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

#acceleration
drive.use_gyro(True)
drive.settings(straight_speed=500, straight_acceleration=[500,100], turn_rate=90, turn_acceleration=[90,45])
drive.straight(600)
drive.turn(180)
drive.angle()
#drive.straight(600, straight_speed=500, straight_acceleration=[500,100])
'''
drive.settings(500, 50)#drive speed, drive acceleration
drive.straight(800)
drive.settings(500, 50, 45, 90) #drive speed, drive acceleration, turn speed, turn acceleration
drive.turn(180)
drive.settings(500, 500)
drive.straight(800)
drive.settings(500, 50, 180)
drive.turn(180)
print("hello world!")
'''

