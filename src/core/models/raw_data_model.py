from dataclasses import dataclass
from typing import List

@dataclass
class RawDataModel:
    bug_id: int
    report_type: str
    status: str
    product: str
    component: str
    platform: str
    summary: str
    description: str
    resolution: str
    severity: str
    priority: str
    duplicates: List[int]