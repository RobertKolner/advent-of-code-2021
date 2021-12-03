import ward

from challenges import day03a, day03b

values_str = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()


@ward.test("day 3a")
def _():
    assert 198 == day03a.run(values_str)


@ward.test("day 3b")
def _():
    assert 230 == day03b.run(values_str)
