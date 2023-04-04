from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    # isso aqui é uma compreension, coloquei quebra de linhas
    # para não estourar a regra do flake8 de linhas máximas
    max_value = list(
        int(row["max_salary"])
        for row in read(path) if row["max_salary"].isdigit()
    )
    return max(max_value)


def get_min_salary(path: str) -> int:
    min_value = list(
        int(row["min_salary"])
        for row in read(path) if row["min_salary"].isdigit()
    )
    return min(min_value)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_value = int(job["min_salary"])
        max_value = int(job["max_salary"])
        if min_value > max_value:
            raise ValueError
        elif min_value <= int(salary) <= max_value:
            return True
        else:
            return False
    except (ValueError, TypeError, KeyError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    all_valid_jobs = []
    for row in jobs:
        try:
            if matches_salary_range(row, salary):
                all_valid_jobs.append(row)
        except ValueError:
            print('')
    return all_valid_jobs
