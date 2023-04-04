from functools import lru_cache
from typing import List, Dict, Set
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        return list(csv.DictReader(file))


def get_unique_job_types(path: str) -> Set[str]:
    return set(row["job_type"] for row in read(path))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return list(row for row in jobs if row["job_type"] == job_type)
