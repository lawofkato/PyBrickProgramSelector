from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#Configure the robot drivebase
perf = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
leftWheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightWheel = Motor(Port.E, Direction.CLOCKWISE)
drive = DriveBase(leftWheel, rightWheel, 30.4, 86)

#drive in a square
drive.use_gyro(True)
count = int(0)
while count < 4:
    drive.straight(300)
    drive.turn(90)
    count += 1
