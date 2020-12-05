# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

# ===================================================================================================
#   CLASS MONEY
# ===================================================================================================

class money:
    """
    """
    def __init__(self, amnt):
        """[summary]

        Parameters
        ----------
        amnt : [type]
            [description]
        """
        self.amnt = int(amnt)

    def get_amnt(self):
        """
        """
        return self.amnt
    
    def amnt_increase(self, incr):
        """[summary]

        Parameters
        ----------
        incr : [type]
            [description]
        """
        self.amnt += incr

    def amnt_decrease(self, decr):
        """[summary]

        Parameters
        ----------
        decr : [type]
            [description]
        """
        self.amnt -= decr

