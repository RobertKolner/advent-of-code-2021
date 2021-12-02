import ward

from challenges import day02a, day02b

values_str = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


@ward.test("day 2a")
def _():
    assert 150 == day02a.run(values_str)


@ward.test("day 2b")
def _():
    assert 900 == day02b.run(values_str)
