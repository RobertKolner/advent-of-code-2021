import collections
import sys


def run(values_str: str):
    paths = [line.split("-") for line in values_str.split("\n") if line]
    connections = collections.defaultdict(set)
    for a, b in paths:
        connections[a].add(b)
        connections[b].add(a)

    def explore(current_path):
        if current_path[-1] == "end":
            yield current_path
        possible_nodes = [
            n for n in connections[current_path[-1]] if n not in current_path or n.isupper()
        ]
        for node in possible_nodes:
            yield from explore(current_path + [node])

    return sum(1 for _ in explore(["start"]))


if __name__ == "__main__":
    print(run(sys.stdin.read()))
