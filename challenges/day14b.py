import collections
import sys


def run(values_str: str):
    template, insertion_bulk = [bulk.strip() for bulk in values_str.split("\n\n") if bulk]
    insertions = dict([line.split(" -> ") for line in insertion_bulk.split("\n") if line])
    pair_counts = collections.Counter("".join([a, b]) for a, b in zip(template, template[1:]))

    for iteration in range(40):
        new_pair_counts = collections.defaultdict(int)
        for pair, count in pair_counts.items():
            new_letter = insertions.get(pair)
            if new_letter:
                new_pair_counts[f"{pair[0]}{new_letter}"] += count
                new_pair_counts[f"{new_letter}{pair[1]}"] += count
            else:
                new_pair_counts[pair] += count
        pair_counts = new_pair_counts

    letter_counts = collections.defaultdict(int)
    for pair, count in pair_counts.items():
        letter_counts[pair[0]] += count
    letter_counts[template[-1]] += 1

    return max(letter_counts.values()) - min(letter_counts.values())


if __name__ == "__main__":
    print(run(sys.stdin.read()))
