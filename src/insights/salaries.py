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
        if job["min_salary"] > job["max_salary"]:
            raise ValueError
        elif job["min_salary"] <= int(salary) <= job["max_salary"]:
            return True
        else:
            return False
    except (ValueError, TypeError, KeyError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
