from gpiozero import AngularServo
from time import sleep

#ear movement 
leftEar = AngularServo(gpio_port=14, min_angle=-90, max_angle=90, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
rightEar = AngularServo(gpio_port=18, min_angle=-90, max_angle=90, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

#neck movement
horiServo = AngularServo(gpio_port=20, min_angle=-90, max_angle=90, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
vertServo = AngularServo(gpio_port=26, min_angle=-90, max_angle=90, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)


def servoAngle(servo, angle):
    servo.angle = angle


def servoRunEars():
    angle = int(input("Enter angle for left ear (0 to 180): "))
    servoAngle(leftEar, angle)
    angle2 = int(input("Enter angle for right ear (0 to 180): "))
    servoAngle(rightEar, angle2)

def servoRunNeck():
    angle = int(input("Enter angle for left-to-right joint (0 to 180): "))
    servoAngle(horiServo, angle)
    angle2 = int(input("Enter angle for up-and-down joint (0 to 180): "))
    servoAngle(vertServo, angle2)


def servoRunTest():
    servoAngle(leftEar, 90)
    servoAngle(rightEar, 90)

def servoReset():
    leftEarAngle = 90
    rightEarAngle = 90
    horiServoAngle = 90
    vertServoAngle = 90
    servoAngle(leftEar, leftEarAngle)
    servoAngle(rightEar, rightEarAngle)
    servoAngle(horiServo, horiServoAngle)
    servoAngle(vertServo, vertServoAngle)
    return leftEarAngle, rightEarAngle, horiServoAngle, vertServoAngle

servoRunNeck()