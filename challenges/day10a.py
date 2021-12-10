import sys


def run(values_str: str):
    lines = [line for line in values_str.split() if line]
    pairings = {"(": ")", "[": "]", "{": "}", "<": ">"}
    point_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    points = 0
    for line in lines:
        stack = []
        for char in line:
            if char in pairings:
                stack.append(char)
            else:
                last_char = stack.pop()
                if char != pairings[last_char]:
                    points += point_map[char]
    return points


if __name__ == "__main__":
    print(run(sys.stdin.read()))
