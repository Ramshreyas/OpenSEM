# Quick Start Guide

This guide will get you up and running with OpenSEM in minutes.

## Prerequisites

*   Python 3.10+
*   A Google Gemini API Key (for the default Data Forge strategy)

## Installation

1.  **Clone the Repository** (or download the source):
    ```bash
    git clone https://github.com/Ramshreyas/OpenSEM.git
    cd OpenSEM
    ```

2.  **Set up a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables**:
    Create a `.env` file in the root directory and add your API key:
    ```bash
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

All commands are run via the `opensem.py` CLI tool.

### 1. Initialize Workspace
If you are starting fresh, initialize the workspace structure:
```bash
python opensem.py init
```

### 2. Create a New Project
Create a container for your specific model task. Let's call it `testsem`.
```bash
python opensem.py new testsem
```
This creates:
*   `configs/testsem/data_config.yaml`
*   `data/testsem/raw/`
*   `data/testsem/processed/`

### 3. Add Data
Place your raw documents (PDF, txt, md) into the project.
```bash
# You can manually copy files or use the helper command (coming soon)
cp my_document.pdf data/testsem/raw/
```

### 4. Run the Data Forge
Synthesize training data from your raw documents.
```bash
python opensem.py run-forge --project testsem
```

Check the output in `data/testsem/processed/train.jsonl`.
