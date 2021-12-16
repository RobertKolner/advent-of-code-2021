import collections
import sys


def run(values_str: str):
    template, insertion_bulk = [bulk.strip() for bulk in values_str.split("\n\n") if bulk]
    insertions = dict([line.split(" -> ") for line in insertion_bulk.split("\n") if line])

    for iteration in range(10):
        result = []
        for left, right in zip(template, template[1:]):
            result.append(left)
            if f"{left}{right}" in insertions:
                result.append(insertions[f"{left}{right}"])
        result.append(template[-1])
        template = "".join(result)

    letter_counts = collections.Counter(template)
    return letter_counts.most_common(1)[0][1] - letter_counts.most_common()[-1][1]


if __name__ == "__main__":
    print(run(sys.stdin.read()))
