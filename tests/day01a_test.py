import ward

import challenges.day01a


@ward.test(__name__)
def _():
    assert 514579 == challenges.day01a.run(
        """1721
        979
        366
        299
        675
        1456"""
    )
