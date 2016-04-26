#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <mysim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *

# Add the MORSE mascott, MORSY.
# Out-the-box available robots are listed here:
# http://www.openrobots.org/morse/doc/stable/components_library.html
#
# 'morse add robot <name> mysim' can help you to build custom robots.
robot =ATRV()#  kuka_lwr()
kuka_arm = KukaLWR()
kuka_arm.translate(x=0.1850, y=0.2000, z=0.9070)
kuka_arm.rotate(x=1.5708, y=1.5708)
robot.append(kuka_arm)
#kuka_arm.translate(x=0.1850, y=0.2000, z=0.9070)
#kuka_arm.rotate(x=1.5708, y=1.5708)
#kuka_arm = KukaLWR()

# The list of the main methods to manipulate your components
# is here: http://www.openrobots.org/morse/doc/stable/user/builder_overview.html
#robot.translate(1.0, 0.0, 0.0)

# Add a motion controller
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
#
# 'morse add actuator <name> mysim' can help you with the creation of a custom
# actuator.
#motion = MotionVW()
#robot.append(motion)


# Add a keyboard controller to move the robot with arrow keys.
#keyboard = Keyboard()
#kuka_arm.append(keyboard)
#keyboard.properties(ControlType = 'Position')
#gripper = Gripper()
#gripper.translate(z=1.2800)
#kuka_arm.append(gripper)

# Add a pose sensor that exports the current location and orientation
# of the robot in the world frame
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#sensors
#
# 'morse add sensor <name> mysim' can help you with the creation of a custom
# sensor.
#pose = Pose()
#pose.translate(z=1)
#kuka_arm.append(pose)

# To ease development and debugging, we add a socket interface to our robot.
#
# Check here: http://www.openrobots.org/morse/doc/stable/user/integration.html 
# the other available interfaces (like ROS, YARP...)
#robot.add_default_interface('socket')


# set 'fastmode' to True to switch to wireframe mode
nv = Environment('enviroment/boxe.blend', fastmode = False)
nv.set_camera_location([10.0, -10.0, 10.0])
nv.set_camera_rotation([1.05, 0, 0.78])

