import ward

from challenges import day15a, day15b

values_str = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip()


@ward.test("day 15a")
def _():
    assert 40 == day15a.run(values_str)


@ward.test("day 15b")
def _():
    assert 315 == day15b.run(values_str)
