import collections
import sys


def run(values_str: str):
    ages = [int(v) for v in values_str.split(",") if v]
    age_map = collections.Counter(ages)
    for _ in range(256):
        new_individuals = age_map.get(0, 0)
        age_map = {k - 1: v for k, v in age_map.items()}
        age_map[6] = age_map.get(6, 0) + age_map.get(-1, 0)
        age_map[8] = new_individuals
        if -1 in age_map:
            del age_map[-1]

    return sum(age_map.values())


if __name__ == "__main__":
    print(run(sys.stdin.read()))
