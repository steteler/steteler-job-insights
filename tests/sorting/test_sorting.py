from src.pre_built.sorting import sort_by
import pytest


jobs_fixture = [
    {
        "min_salary": 10,
        "max_salary": 20,
        "date_posted": "2023-01-02",
        "job_title": "Back End Developer",
    },
    {
        "min_salary": 1,
        "max_salary": 25,
        "date_posted": "2022-01-02",
        "job_title": "Front End Developer",
    },
    {
        "min_salary": 150,
        "max_salary": 200,
        "date_posted": "2021-01-02",
        "job_title": "Full Stack Developer",
    },
]


@pytest.fixture
def jobs():
    return jobs_fixture


def test_sort_by_criteria(jobs):
    job_list = jobs
    sort_by(job_list, "max_salary")
    assert job_list[0]["job_title"] == "Full Stack Developer"
    assert job_list[2]["job_title"] == "Back End Developer"
