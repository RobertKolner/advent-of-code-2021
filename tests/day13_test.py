import ward

from challenges import day13a, day13b

values_str = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""".strip()


@ward.test("day 13a")
def _():
    assert 17 == day13a.run(values_str)


@ward.test("day 13b")
def _():
    ...
    assert day13b.run(values_str) is None  # The puzzle output is read manually
