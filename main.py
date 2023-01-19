from TwoJointArm import TwoJointArm
from Translation2d import Translation2d
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numpy as np

arm = TwoJointArm(10, 5)
x = 10
y = 10

figure, axis = plt.subplots(1, 2)


def animate(i):
    global y, x

    angles = arm.calculate_angles(Translation2d(x, y))

    elbow_x = math.cos(angles[0]) * arm.elbow_length
    elbow_y = math.sin(angles[0]) * arm.elbow_length

    elbow_x_neg = math.cos(angles[2]) * arm.elbow_length
    elbow_y_neg = math.sin(angles[2]) * arm.elbow_length

    wrist_x = math.cos(angles[0] + angles[1]) * arm.wrist_length + elbow_x
    wrist_y = math.sin(angles[0] + angles[1]) * arm.wrist_length + elbow_y

    wrist_x_neg = math.cos(angles[2] + angles[3]) * \
        arm.wrist_length + elbow_x_neg
    wrist_y_neg = math.sin(angles[2] + angles[3]) * \
        arm.wrist_length + elbow_y_neg

    axis[0].clear()
    axis[0].plot([10, -10], [10, 10], color="grey")
    axis[0].plot([0, elbow_x], [0, elbow_y], color="blue")
    axis[0].plot([elbow_x, wrist_x], [elbow_y, wrist_y], color="red")
    axis[0].set_title(f'X = {round(x, 3)}, Y = {round(y, 3)} POSITIVE')

    axis[0].set_xticks(np.arange(-10, 11, 2))
    axis[0].set_yticks(np.arange(-10, 11, 2))
    axis[0].set_aspect('equal', 'box')

    axis[1].clear()
    axis[1].plot([10, -10], [10, 10], color="grey")
    axis[1].plot([0, elbow_x_neg], [0, elbow_y_neg], color="blue")
    axis[1].plot([elbow_x_neg, wrist_x_neg],
                 [elbow_y_neg, wrist_y_neg], color="red")
    axis[1].set_title(f'X = {round(x, 3)}, Y = {round(y, 3)} NEGATIVE')
    axis[1].set_xticks(np.arange(-10, 11, 2))
    axis[1].set_yticks(np.arange(-10, 11, 2))
    axis[1].set_aspect('equal', 'box')

    x -= 1 / (1000 / 60)


ani = animation.FuncAnimation(figure, animate, interval=1000 / 60, frames=9*60)

ani.save("test7.mp4", fps=30)
plt.show()
