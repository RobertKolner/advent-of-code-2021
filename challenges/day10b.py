import sys


def run(values_str: str):
    lines = [line for line in values_str.split() if line]
    pairings = {"(": ")", "[": "]", "{": "}", "<": ">"}
    point_map = {")": 1, "]": 2, "}": 3, ">": 4}
    points_per_line = []
    for line in lines:
        stack = []
        for char in line:
            if char in pairings:
                stack.append(char)
            else:
                last_char = stack.pop()
                if char != pairings[last_char]:
                    break
        else:  # no break
            points = 0
            for char in reversed(stack):
                points *= 5
                points += point_map[pairings[char]]
            points_per_line.append(points)
    return sorted(points_per_line)[len(points_per_line) // 2]


if __name__ == "__main__":
    print(run(sys.stdin.read()))
