from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#hub = PrimeHub()
#configure Perf Hub for drivebase and attachments + sensors
perf = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
leftwheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightwheel = Motor(Port.E, Direction.CLOCKWISE)
drivebase = DriveBase(leftwheel, rightwheel, 30.4, 86)
armMotor = Motor(Port.C, Direction.CLOCKWISE)
leftEye = ColorSensor(Port.B)
rightEye = ColorSensor(Port.F)
distanceSensor = UltrasonicSensor(Port.D)

drivebase.straight(0)
drivebase.use_gyro(True)
drivebase.settings(turn_rate=180)
drivebase.settings(straight_speed=400, straight_acceleration=[200,200])

offSetValue = float(0.1)

def gyroTurn(degrees):
    drivebase.turn(degrees)
    print(perf.imu.heading())

def gyroTurnCorrection(degreeAngle):
    lowValue = degreeAngle - offSetValue
    print ("LowValue = " + str(lowValue))
    highValue = degreeAngle + offSetValue
    print ("HighValue = " + str(highValue))
    print ("StartValue = " + str(perf.imu.heading()))
    drivebase.turn(degreeAngle)
    print ("ValueAfterTurn = " + str(perf.imu.heading()))
    targetValue = float(0)
    if degreeAngle < perf.imu.heading():
        #targetValue = perf.imu.heading() - degreeAngle
        targetValue = degreeAngle - perf.imu.heading() - offSetValue
        print ("TargetValueFound = " + str(targetValue))
    else:
        #targetValue = degreeAngle - perf.imu.heading()
        targetValue = perf.imu.heading() - degreeAngle - offSetValue
        print ("TargetValueFound = " + str(targetValue))
    
    if not (lowValue <= perf.imu.heading() <= highValue):
        drivebase.settings(turn_rate=90)
        #targetValue = abs(targetValue)
        print (str(targetValue))
        drivebase.turn(targetValue,then=Stop.HOLD)
        print ("FinalValue = " + str(perf.imu.heading()))
        drivebase.settings(turn_rate=90)

def driveSquare():
    print(perf.imu.heading())
    x = 0
    while x < 4:
        drivebase.straight(300)
        drivebase.turn(90)
        print(perf.imu.heading())
        x += 1


perf.imu.reset_heading(0)
print(perf.imu.heading())

drivebase.straight(300)
gyroTurnCorrection(90)


#driveSquare()

'''
drivebase.straight(500)
print(perf.imu.heading())
drivebase.turn(90)
print("after turn right 90 degrees")
print(perf.imu.heading())
gyroTurn(-45)'''
#raise SystemExit