import collections
import sys


def run(values_str: str):
    paths = [line.split("-") for line in values_str.split("\n") if line]
    connections = collections.defaultdict(set)
    for a, b in paths:
        connections[a].add(b)
        connections[b].add(a)

    explored_paths = set()

    def explore(current_path, allow_double=True):
        if current_path[-1] == "end":
            if ",".join(current_path) not in explored_paths:
                yield current_path
            explored_paths.add(",".join(current_path))
            return
        possible_nodes = [
            n
            for n in connections[current_path[-1]]
            if n != "start" and (n.isupper() or allow_double or n not in current_path)
        ]
        for node in possible_nodes:
            yield from explore(
                current_path + [node],
                False if node.islower() and node in current_path else allow_double,
            )

    return sum(1 for _ in explore(["start"]))


if __name__ == "__main__":
    print(run(sys.stdin.read()))
