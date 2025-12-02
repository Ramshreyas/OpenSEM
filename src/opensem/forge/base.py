from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseForge(ABC):
    """
    Abstract Base Class for Data Forge strategies.
    Defines the contract for ingesting, synthesizing, and formatting data.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the forge with configuration parameters.
        
        Args:
            config: Dictionary containing configuration parameters (e.g., paths, model names).
        """
        self.config = config

    @abstractmethod
    def load_data(self) -> Any:
        """
        Load raw data from the source directory.
        
        Returns:
            The loaded data in an intermediate format suitable for synthesis.
        """
        pass

    @abstractmethod
    def synthesize(self, raw_data: Any) -> List[Dict[str, Any]]:
        """
        Synthesize instruction-output pairs from the raw data.
        
        Args:
            raw_data: The data returned by load_data().
            
        Returns:
            A list of dictionaries representing the synthesized dataset.
        """
        pass

    @abstractmethod
    def format_data(self, synthesized_data: List[Dict[str, Any]]) -> None:
        """
        Format the synthesized data into the final training format (e.g., JSONL)
        and save it to the processed directory.
        
        Args:
            synthesized_data: The data returned by synthesize().
        """
        pass

    def run(self):
        """
        Execute the full data processing pipeline.
        """
        print(f"[{self.__class__.__name__}] Starting Data Forge pipeline...")
        
        print(f"[{self.__class__.__name__}] Loading data...")
        raw_data = self.load_data()
        
        print(f"[{self.__class__.__name__}] Synthesizing data...")
        synthesized_data = self.synthesize(raw_data)
        
        print(f"[{self.__class__.__name__}] Formatting and saving data...")
        self.format_data(synthesized_data)
        
        print(f"[{self.__class__.__name__}] Pipeline completed successfully.")
