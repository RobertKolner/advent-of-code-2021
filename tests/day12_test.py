import ward

from challenges import day12a, day12b

values_str = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".strip()


@ward.test("day 12a")
def _():
    assert 10 == day12a.run(values_str)


@ward.test("day 12b")
def _():
    assert 36 == day12b.run(values_str)
