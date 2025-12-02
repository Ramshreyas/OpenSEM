import os
import glob
import json
from typing import Any, Dict, List
from dotenv import load_dotenv
import google.generativeai as genai
from .base import BaseForge

class TextForge(BaseForge):
    """
    Default Data Forge strategy for processing text documents (.txt, .md, .pdf).
    """

    def load_data(self) -> List[str]:
        """
        Load text files from the configured raw data directory.
        """
        raw_dir = self.config.get("raw_data_dir", "data/raw")
        if not os.path.exists(raw_dir):
            raise FileNotFoundError(f"Raw data directory not found: {raw_dir}")

        files = glob.glob(os.path.join(raw_dir, "*.txt")) + \
                glob.glob(os.path.join(raw_dir, "*.md")) + \
                glob.glob(os.path.join(raw_dir, "*.pdf"))
        
        documents = []
        for file_path in files:
            if file_path.endswith(".pdf"):
                try:
                    import pypdf
                    reader = pypdf.PdfReader(file_path)
                    text = ""
                    for page in reader.pages:
                        text += page.extract_text() + "\n"
                    documents.append(text)
                except ImportError:
                    print(f"Warning: pypdf not installed. Skipping PDF file: {file_path}")
                except Exception as e:
                    print(f"Error reading PDF {file_path}: {e}")
            else:
                with open(file_path, "r", encoding="utf-8") as f:
                    documents.append(f.read())
        
        print(f"Loaded {len(documents)} documents from {raw_dir}")
        return documents

    def synthesize(self, raw_data: List[str]) -> List[Dict[str, Any]]:
        """
        Synthesize instruction pairs from text documents using Gemini API.
        """
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            print("Warning: GEMINI_API_KEY not found in .env. Using mock synthesis.")
            return self._mock_synthesize(raw_data)

        try:
            genai.configure(api_key=api_key)
            
            # Get config params
            params = self.config.get('params', {})
            model_name = params.get('teacher_model', 'gemini-1.5-flash')
            max_chars = params.get('max_chars_per_doc', 10000)
            chunk_size = params.get('chunk_size', 5000)

            model = genai.GenerativeModel(model_name)
            
            synthesized_data = []
            print(f"Synthesizing data using {model_name}...")
            print(f"Limits: max_chars={max_chars}, chunk_size={chunk_size}")

            for i, doc in enumerate(raw_data):
                # Apply character limit per document
                doc_to_process = doc[:max_chars]
                
                # Create chunks
                chunks = [doc_to_process[j:j+chunk_size] for j in range(0, len(doc_to_process), chunk_size)]
                
                for j, chunk in enumerate(chunks):
                    print(f"Processing document {i+1}, chunk {j+1}/{len(chunks)}...")
                    prompt = f"""
                    You are an expert data synthesizer for training Small Language Models.
                    Your task is to generate 3 high-quality instruction-response pairs based on the following text.
                    The goal is to teach a model to reason about this specific content.
                    
                    Output MUST be a valid JSON array of objects with keys: "instruction", "input", "output".
                    "input" should be empty string unless context is absolutely necessary.
                    
                    Text:
                    {chunk}
                    """
                    
                    try:
                        response = model.generate_content(prompt)
                        text = response.text.strip()
                        # Clean up markdown code blocks if present
                        if text.startswith("```json"):
                            text = text[7:]
                        if text.startswith("```"):
                            text = text[3:]
                        if text.endswith("```"):
                            text = text[:-3]
                        
                        pairs = json.loads(text.strip())
                        synthesized_data.extend(pairs)
                    except Exception as e:
                        print(f"Error synthesizing chunk {j} of document {i}: {e}")
            
            return synthesized_data

        except Exception as e:
            print(f"Failed to initialize Gemini: {e}")
            return self._mock_synthesize(raw_data)

    def _mock_synthesize(self, raw_data: List[str]) -> List[Dict[str, Any]]:
        print("Synthesizing data (Mock Implementation)...")
        synthesized_data = []
        for i, doc in enumerate(raw_data):
            synthesized_data.append({
                "instruction": f"Summarize document {i}",
                "input": "",
                "output": doc[:100] + "..." 
            })
        return synthesized_data

    def format_data(self, synthesized_data: List[Dict[str, Any]]) -> None:
        """
        Save data to JSONL format, splitting into train/test.
        """
        processed_dir = self.config.get("processed_data_dir", "data/processed")
        os.makedirs(processed_dir, exist_ok=True)
        
        # Simple 90/10 split
        split_idx = int(len(synthesized_data) * 0.9)
        train_data = synthesized_data[:split_idx]
        test_data = synthesized_data[split_idx:]
        
        train_path = os.path.join(processed_dir, "train.jsonl")
        test_path = os.path.join(processed_dir, "test.jsonl")
        
        self._save_jsonl(train_data, train_path)
        self._save_jsonl(test_data, test_path)
        
        print(f"Saved {len(train_data)} training examples to {train_path}")
        print(f"Saved {len(test_data)} test examples to {test_path}")

    def _save_jsonl(self, data: List[Dict[str, Any]], path: str):
        with open(path, "w", encoding="utf-8") as f:
            for entry in data:
                f.write(json.dumps(entry) + "\n")
