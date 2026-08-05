from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

# neutral pan angle = 90
# looking to my right = 180
# looking to my left = 0
# port 0

# neutral tilt angle = 130
# looking up angle = 180
# looking down angle = 0
# port 1

# perked left ear angle = 0
# neutral left ear angle = 50
# sad left ear angle = 180
# port 2

# perked right ear angle = 180
# neutral right ear angle = 130
# sad right ear angle = 0
# port 3

panServo = kit.servo[0]
tiltServo = kit.servo[1]

leftEar = kit.servo[2]
rightEar = kit.servo[3]


def happyEars():
    leftEar.angle = 0
    rightEar.angle = 180

def neutralEars():
    leftEar.angle = 50
    rightEar.angle = 130

def neutralStance():
    leftEar.angle = 50
    rightEar.angle = 130
    panServo.angle = 90
    tiltServo.angle = 130

def sadEars():
    leftEar.angle = 180
    rightEar.angle = 0
