import ward

from challenges import day09a, day09b

values_str = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()


@ward.test("day 9a")
def _():
    assert 15 == day09a.run(values_str)


@ward.test("day 9b")
def _():
    assert 1134 == day09b.run(values_str)
