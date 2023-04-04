from src.pre_built.counter import count_ocurrences


def test_counter():
    ocurrences = count_ocurrences('data/jobs.csv', "Python")
    assert ocurrences == 1639
