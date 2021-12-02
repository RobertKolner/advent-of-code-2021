import ward

import challenges.day02b as fn


@ward.test(__name__)
def _():
    assert 900 == fn.run(
        """forward 5
           down 5
           forward 8
           up 3
           down 8
           forward 2"""
    )
