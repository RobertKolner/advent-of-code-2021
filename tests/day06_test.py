import ward

from challenges import day06a, day06b

values_str = """3,4,3,1,2"""


@ward.test("day 6a")
def _():
    assert 5934 == day06a.run(values_str)


@ward.test("day 6b")
def _():
    ...
    assert 26984457539 == day06b.run(values_str)
