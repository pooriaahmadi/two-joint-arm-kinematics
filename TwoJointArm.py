from typing import List
from Translation2d import Translation2d
import math


class TwoJointArm:
    def __init__(self, elbow_length: float, wrist_length: float, tooltip_position: Translation2d = None) -> None:
        self.elbow_length = elbow_length
        self.wrist_length = wrist_length
        self.tooltip_position = tooltip_position

    def calculate_angles(self, tooltip_position: Translation2d) -> List[int]:
        self.tooltip_position = tooltip_position
        ## POSITIVE ##
        # Wrist angle
        q2 = (tooltip_position.x**2 + tooltip_position.y**2 - self.elbow_length **
              2 - self.wrist_length**2) / (2 * self.elbow_length * self.wrist_length)
        q2 = math.acos(q2)

        # Elbow angle
        q1 = math.atan(tooltip_position.y / tooltip_position.x) - math.atan(
            (self.wrist_length * math.sin(q2)) / (self.wrist_length * math.cos(q2) + self.elbow_length))

        ## NEGATIVE ##
        # Elbow angle
        q1_different = math.atan(tooltip_position.y / tooltip_position.x) + math.atan(
            (self.wrist_length * math.sin(q2)) / (self.wrist_length * math.cos(q2) + self.elbow_length))

        return [q1, q2, q1_different, -q2]
