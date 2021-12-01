import ward

import challenges.day01b


@ward.test(__name__)
def _():
    assert 5 == challenges.day01b.run(
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
