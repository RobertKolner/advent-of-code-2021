import ward

from challenges import day11a, day11b

values_str = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip()


@ward.test("day 11a")
def _():
    assert 1656 == day11a.run(values_str)


@ward.test("day 11b")
def _():
    assert 195 == day11b.run(values_str)
