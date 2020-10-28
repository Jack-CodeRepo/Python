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


    def lost_limb(self, limbs, sides):
        sides_list = sides.split(",")
        limb_list = limbs.split(",")
        for limb in limb_list:
            for side in sides_list:
                self.${side}_${limb}.limb_exist" = False




    #     self.rightArm = ub.arms("right")
    #     self.leftArm = ub.arms("left")

    #     self.rightLeg = lb.legs("right")
    #     self.leftLeg = lb.legs("left")


    # def lost_limb(self, limb, sides):
    #     sides_list = sides.split(",")
    #     if limb == "arm":
    #         for side in sides_list:
    #             self.lost_arm(side)

    # def lost_arm(self, side):
    #     if side == "right":
    #         self.rightLeg.leg_exist = False
    #     if side == "left":
    #         self.leftLeg.leg_exist = False

    # def lost_leg(self, side):
    #     if side == "right":
    #         self.rightArm.arm_exist = False
    #     if side == "left":
    #         self.leftArm.arm_exist = False


    # def check_limb(self):
    #     print(f"Le cote {self.rightArm.arm_side} est {self.rightArm.arm_exist}")
    #     print(f"Le cote  {self.leftArm.arm_side} est {self.leftArm.arm_exist}")
    #     print(f"Le cote  {self.rightLeg.leg_side} est {self.rightLeg.leg_exist}")
    #     print(f"Le cote  {self.leftLeg.leg_side} est {self.leftLeg.leg_exist}")






# ==================================================================================================
#   SCRIPT
# ==================================================================================================

corps()