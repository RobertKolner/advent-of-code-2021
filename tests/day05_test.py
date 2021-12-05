import ward

from challenges import day05a, day05b

values_str = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip()


@ward.test("day 5")
def _():
    assert 5 == day05a.run(values_str)


@ward.test("day 4b")
def _():
    assert 12 == day05b.run(values_str)
