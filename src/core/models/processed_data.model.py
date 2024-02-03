from dataclasses import dataclass
from typing import List

@dataclass
class ProcessedData:
  text: str
  text_embedded: List[int]
  duplicates_to = int