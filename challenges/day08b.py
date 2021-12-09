import itertools
import sys


def run(values_str: str):
    displays = [
        [
            ["".join(sorted(number.strip())) for number in segment.split(" ") if number.strip()]
            for segment in line.split("|")
            if segment.strip()
        ]
        for line in values_str.split("\n")
        if line.strip()
    ]

    number_value = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }

    all_outputs = 0
    for inputs, outputs in displays:

        def test_mapping(mapping):
            for number in inputs:
                mapped_segments = "".join(sorted(mapping[segment] for segment in number))
                if mapped_segments not in number_value:
                    return False
            return True

        true_mapping = None
        for combination in itertools.permutations("abcdefg"):
            potential_mapping = {k: v for k, v in zip("abcdefg", combination)}
            if test_mapping(potential_mapping):
                true_mapping = potential_mapping
                break

        if not true_mapping:
            continue

        numbers = [
            number_value["".join(sorted(true_mapping[segment] for segment in number))]
            for number in outputs
        ]
        number = 0
        for index, n in enumerate(reversed(numbers)):
            number += n * 10 ** index
        all_outputs += number
    return all_outputs


if __name__ == "__main__":
    print(run(sys.stdin.read()))
