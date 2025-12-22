from gpiozero import AngularServo
from time import sleep

leftEar = AngularServo(18, min_angle=-90, max_angle=90, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
rightEar = AngularServo(12, min_angle=-90, max_angle=90, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)


def servoAngle(servo, angle):
    servo.angle = angle
    sleep(1)

def servoRun():
    try:
        while True:
            angle = int(input("Enter angle (0 to 180): "))
            servoAngle(leftEar, angle)
    except KeyboardInterrupt:
	    print("Program stopped by user")

servoRun()