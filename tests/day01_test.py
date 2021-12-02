import ward

from challenges import day01a, day01b

values_str = """
199
200
208
210
200
207
240
269
260
263"""


@ward.test("day 1a")
def _():
    assert 7 == day01a.run(values_str)


@ward.test("day 1b")
def _():
    assert 5 == day01b.run(values_str)
