import ward

from challenges import day14a, day14b

values_str = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip()


@ward.test("day 14a")
def _():
    assert 1588 == day14a.run(values_str)


@ward.test("day 14b")
def _():
    assert 2188189693529 == day14b.run(values_str)
