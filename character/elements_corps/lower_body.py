# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================



# ==================================================================================================
#   VARIABLES GLOBALES
# ==================================================================================================




# ==================================================================================================
#   DICT
# ==================================================================================================


# ==================================================================================================
#   LISTS
# ==================================================================================================


# ==================================================================================================
#   FONCTIONS
# ==================================================================================================


# ==================================================================================================
#   CLASSES
# ==================================================================================================

class legs():
    def __init__(self, side):

        self._exists = True
        self._side = side

    @property
    def leg_exist(self):
        return self._exists

    @leg_exist.setter
    def leg_exist(self, value):
        self._exists = value

    @property
    def leg_side(self):
        return self._side

    @leg_side.setter
    def leg_side(self, value):
        self._side = value





# ==================================================================================================
#   SCRIPT
# ==================================================================================================
