#
# author: Tristan Brideweser
# date: 12/6/2024
# course: MFET 348

import roboticstoolbox as rtb
import swift
import spatialmath as sm
import numpy as np
import pybullet as p
import pybullet_data
import time

# Project Goals
# -------------------------------------------------------------------
# create robot object (DONE)
# define robot start position
#   base and end effector
# define robot goal position
#   base and end effector
# define robot trajectory start ---> goal
# create kitchen environment (DONE)
# outline DH parameters (DONE, accessible via rtb.models.DH.Panda())

def setup():
    """
    Create environment and load robot
    :return:
    """

    env = swift.Swift()
    env.launch(realtime=True)
    panda = rtb.models.URDF.Panda()

    env.add(panda)

    start_pos(panda)

    while True:
        env.step(0.05)


def start_pos(robot):
    """
    Define robot start position for base and end effector
    :return:
    """

    # zero joint config
    qz = robot.qz

    # set joints to home position
    robot.q = qz

def end_pos():
    """
    Define robot end position for base and end effector
    :return:
    """
    pass


def trajectory(start, end):
    """
    Define robot trajectory
    :param start:
    :param end:
    :return:
    """
    pass


def main():
    setup()


if __name__ == '__main__':
    main()
