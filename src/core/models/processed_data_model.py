from dataclasses import dataclass
from typing import List

@dataclass
class ProcessedDataModel:
  text: str
  text_embedded: List[int]
  duplicates_to = int