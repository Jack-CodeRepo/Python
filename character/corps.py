# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import elements_corps.lower_body as lb
import elements_corps.upper_body as ub
import elements_corps.limbs as limbs

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


class corps():
    def __init__(self):
        self.right_arm = limbs.limbs("arm", "right")
        self.left_arm = limbs.limbs("arm", "right")
        self.right_leg = limbs.limbs("leg", "right")
        self.left_leg = limbs.limbs("leg", "right")


    def check_arms(self):
        if not self.right_arm.limb_exist:
            print("Right arm is dead")
        elif not self.left_arm.limb_exist:
            print("Left arm is dead")
        elif not self.right_arm.limb_exist and not self.left_arm.limb_exist:
            print("Both arms are dead")
        else:
            print("All you arms are great")


    def check_leg(self):
        if not self.right_leg.limb_exist:
            print("Right arm is dead")
        elif not self.left_leg.limb_exist:
            print("Left arm is dead")
        elif not self.right_leg.limb_exist and not self.left_leg.limb_exist:
            print("Both arms are dead")
        else:
            print("All you arms are great")


# ==================================================================================================
#   SCRIPT
# ==================================================================================================
