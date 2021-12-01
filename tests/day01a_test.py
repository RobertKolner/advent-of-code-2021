import ward

import challenges.day01a


@ward.test(__name__)
def _():
    assert 7 == challenges.day01a.run(
        """199
200
208
210
200
207
240
269
260
263"""
    )
