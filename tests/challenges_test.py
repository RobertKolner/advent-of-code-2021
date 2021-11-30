import ward

import challenges.day01a
import fixtures

for day, v, fn, exp in (("1", "a", challenges.day01a.run, 55776),):

    @ward.test(f"Test challenge {day}{v}")
    def _():
        fixture = fixtures.load("2020", day)
        assert exp == fn(fixture)
