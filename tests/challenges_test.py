import ward

import challenges.day01a
import challenges.day01b
import fixtures

for day, v, fn, exp in (
    ("1", "a", challenges.day01a.run, 1692),
    ("1", "b", challenges.day01b.run, 1724),
):

    @ward.test(f"Test challenge {day}{v}")
    def _(challenge_function=fn, expected=exp):
        fixture = fixtures.load("2021", day)
        assert expected == challenge_function(fixture)
