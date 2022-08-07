# Documentation

## Labview - ZMQ API 

cRio IP: 192.168.69.40:5555

## Commands:

### Home
**Message:** DeltaRobot>Home>

Homes the deltarobot to the default position.

### Move
**Message:** DeltaRobot>Move>X:Y:Z>Velocity:Acceleration:decelleration>

Moves the deltarobot to the given coordinates with the given velocity, acceleration and decelleration.

*example*: DeltaRobot>Move>30:-20:-330>50:30:60>

### DisableAxis
**Message:** DeltaRobot>DisableAxis>

Disables all the axis thus no current will flow through the motor and it can be moved by hand if you are big boi.

When executing a Home or Move command the axis will automatically enable.

### HomePosition
**Message:** DeltaRobot>HomePosition>theta1:theta2:theta3>

This changes the motors theta angles for the home position. When you home it sets the current angle to this number.

Use this when you change the upper range of the robot arms.

If you change the home angle, this command needs to be executed every time the program reboots.

This only updates the angle variable and doesn't home the robot.

### Stop
**Message:** DeltaRobot>DisableAxis>

Stops the real-time labview program, you will have restart the robot to start the program again.
