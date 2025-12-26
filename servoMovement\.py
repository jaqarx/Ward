from gpiozero import AngularServo
from time import sleep

leftEar = AngularServo(14, min_angle=-90, max_angle=90, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
rightEar = AngularServo(18, min_angle=-90, max_angle=90, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)


def servoAngle(servo, angle):
    servo.angle = angle

def servoRun():
    angle = int(input("Enter angle for left ear (0 to 180): "))
    servoAngle(leftEar, angle)
    angle2 = int(input("Enter angle for right ear (0 to 180): "))
    servoAngle(rightEar, angle2)

def servoRunTest():
    servoAngle(leftEar, 90)
    servoAngle(rightEar, 90)

servoRun()