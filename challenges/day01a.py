import itertools


def run(values_str: str):
    values = [int(v) for v in values_str.split("\n") if v]

    for a, b in itertools.combinations(values, 2):
        if a + b == 2020:
            return a * b
