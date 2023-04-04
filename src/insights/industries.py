from typing import List, Dict, Set
from src.insights.jobs import read


def get_unique_industries(path: str) -> Set[str]:
    return set(row["industry"] for row in read(path) if len(row["industry"]))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
