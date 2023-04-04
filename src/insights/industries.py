from typing import List, Dict, Set
from src.insights.jobs import read


def get_unique_industries(path: str) -> Set[str]:
    return set(row["industry"] for row in read(path) if len(row["industry"]))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return list(row for row in jobs if row["industry"] == industry)
