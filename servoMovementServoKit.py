from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

# neutral pan angle = 90
# looking to my right = 180
# looking to my left = 0
# port 0

# neutral tilt angle = 130
# port 1

# neutral left ear angle = 0
# down left ear angle = 180
# port 2

# neutral right ear angle = 180
# down right ear angle = 0
# port 3



# kit.servo[1].angle=130
kit.servo[0].angle=180

