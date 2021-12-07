import ward

from challenges import day07a, day07b

values_str = """16,1,2,0,4,2,7,1,2,14"""


@ward.test("day 7a")
def _():
    assert 37 == day07a.run(values_str)


@ward.test("day 7b")
def _():
    assert 168 == day07b.run(values_str)
