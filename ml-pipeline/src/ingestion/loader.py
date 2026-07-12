from pathlib import Path
from typing import Any

from datasets import Dataset, load_dataset, load_from_disk

class EnterpriseDatasetLoader:
    def __init__(self):
        self.dataset: Dataset | None=None

    def load_from_disk(self,dataset_path: str|Path)->Dataset:
        dataset_path = Path(dataset_path)
        if not dataset_path.exists():
            raise ValueError(f"Dataset not found {dataset_path}")
        self.dataset = load_from_disk(str(dataset_path))
        return self.dataset
    
    def load_from_huggingface(
        self,
        dataset_name: str,
        split: str = "train",
        ) -> Dataset:

        self.dataset = load_dataset(
            dataset_name,
            split=split,
        )

        return self.dataset
    
    def get_dataset(self) -> Dataset:
        if self.dataset is None:
            raise ValueError("Dataset has not been loaded.")

        return self.dataset

    def num_documents(self) -> int:

        return len(self.get_dataset())

    def features(self):

        return self.get_dataset().features

    def source_types(self) -> list[str]:

        dataset = self.get_dataset()

        if "source_type" not in dataset.column_names:
            return []

        return sorted(set(dataset["source_type"]))

    def sample(self, index: int = 0) -> dict[str, Any]:

        return self.get_dataset()[index]
