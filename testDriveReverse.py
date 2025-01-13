from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#hub = PrimeHub()

perf = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
leftwheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightwheel = Motor(Port.E, Direction.CLOCKWISE)
drivebase = DriveBase(leftwheel, rightwheel, 30.4, 86)

perf.imu.reset_heading(0)
print(perf.imu.heading())
drivebase.straight(0)
drivebase.use_gyro(True)
drivebase.settings(turn_rate=90)
drivebase.settings(straight_speed=200)

drivebase.straight(-500)
raise SystemExit