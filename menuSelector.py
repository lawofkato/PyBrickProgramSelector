from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

hub = PrimeHub()

selected = hub_menu("1", "2", "3")

if selected == "1":
    import testDriveForward

if selected == "2":
    import testDriveReverse

if selected == "3":
    import learning3
