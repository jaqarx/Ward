# **Setting Up the “Ear” Motors**

| Table of Contents | Related Documents |
|---|---|
| [Overview](#overview) | [Building a Creature-like, Face-Detection Robot Using Raspberry Pi (Home Page)](README.md) |
| [Installing the Required Packages](#installing-the-required-packages) | [Required Materials](required-materials.md) |
| [Setting Up the “Ear” Movement Script](#setting-up-the-ear-movement-script) | [Setting up the Hardware](hardware-set-up.md) |
| [Testing the Program](#testing-the-program) | [Setting up the Raspberry Pi and the Raspberry Pi Camera](rasp-pi-set-up.md) |
| [Integrating Servo Movement into the Vision](#integrating-servo-movement-into-the-vision) | [Setting up the Robot's Vision](robot-vision.md) |
| | [Frequently Answered Questions](faq.md) |

## **Overview**

This tutorial is intended for both intermediate and beginner programmers who may or may not have prior experience with servo motors or Python libraries. You should be comfortable running commands in the terminal and have a basic understanding of Python syntax, such as variables, loops, and functions.

For intermediate programmers, all steps are highlighted in bold font. For beginner programmers, additional explanations after the bolded text are included to describe the purpose of each step.

In this tutorial, you will write a Python script to control the robot's "ear" servo motors, test that they move correctly, and then integrate the servo movement into the vision script you wrote in [*Setting Up the Robot's Vision*](https://docs.google.com/document/d/1UGiC80ufGEso83c7PnFgwOVApgB1t09mBcOQ6ye1Nho/edit?tab=t.8d5hcm3tyhk0).

**Prerequisites:**

* Raspberry Pi 5 with the OS installed, up to date, connected to a powered display monitor, and with Camera Module 3 connected and detected (see [*Setting Up the Raspberry Pi and the Raspberry Pi Camera*](https://docs.google.com/document/d/1UGiC80ufGEso83c7PnFgwOVApgB1t09mBcOQ6ye1Nho/edit?tab=t.0))  
* Servo motors connected to GPIO pins 14 and 18 and a power source (see [*Setting Up the Hardware*](https://docs.google.com/document/d/1UGiC80ufGEso83c7PnFgwOVApgB1t09mBcOQ6ye1Nho/edit?tab=t.ogwc9fc1zjum))  
* USB-A mouse and keyboard connected to the Raspberry Pi  
* VSCode installed (see *Installing VSCode* in [*Setting Up the Raspberry Pi and the Raspberry Pi Camera*](https://docs.google.com/document/d/1UGiC80ufGEso83c7PnFgwOVApgB1t09mBcOQ6ye1Nho/edit?tab=t.0))  
* A completed `robotFunctions.py` file from [*Setting Up the Robot's Vision*](https://docs.google.com/document/d/1UGiC80ufGEso83c7PnFgwOVApgB1t09mBcOQ6ye1Nho/edit?tab=t.8d5hcm3tyhk0)

## **Installing the Required Packages**

Before running any scripts, you will need to install the following package on your Raspberry Pi. Open the terminal and run the command below:

* `sudo apt install -y python3-gpiozero`

The **gpiozero** package is used to control the servo motors.

If no error message appears during or after the installation process, the package is installed correctly.

## **Setting Up the “Ear” Movement Script**

1) **Create a new file called** `servoMovement.py` **in the same directory as your** `robotFunctions.py` **file.**

Both files need to be in the same directory so they can import from each other later.

2) **Import the following packages.**

from gpiozero import AngularServo  
from time import sleep

`gpiozero` is a library that makes it easy to control hardware connected to the Raspberry Pi's GPIO pins. `AngularServo` is a class within that library specifically designed for servo motors that move to a set angle. `sleep` lets us pause the program for a set amount of time, which is useful when testing servo movement.

3) **Initialize the left and right ear motors using the code below.**  
   
```
leftEar \= AngularServo(14, min\_angle\=-90, max\_angle\=90, min\_pulse\_width\=0.5/1000, max\_pulse\_width\=2.5/1000)  
rightEar \= AngularServo(18, min\_angle\=-90, max\_angle\=90, min\_pulse\_width\=0.5/1000, max\_pulse\_width\=2.5/1000)
```

This creates two servo objects, one for each ear, and tells the Raspberry Pi how to communicate with them. Here is what each parameter does:

* **GPIO port (`14`, `18`):** The GPIO pin number the servo's signal wire is connected to. The left ear is on pin 14 and the right ear is on pin 18, matching the wiring you did in [*Setting Up the Hardware*](https://docs.google.com/document/d/1UGiC80ufGEso83c7PnFgwOVApgB1t09mBcOQ6ye1Nho/edit?tab=t.ogwc9fc1zjum).  
* **`min_angle` and `max_angle`:** The range of motion for the servo, in degrees. Here you set it to \-90 to 90, giving the servo a full 180 degrees of movement.  
* **`min_pulse_width` and `max_pulse_width`:** These tell the Raspberry Pi what PWM signal to send to move the servo to its minimum and maximum angles. The values `0.5/1000` and `2.5/1000` are standard pulse widths (in seconds) for most hobby servo motors. They correspond to 0.5ms and 2.5ms respectively.

4) **Define the functions below**

```
def servoAngle(servo, angle):  
   servo.angle \= angle

def servoRun():  
   angle \= int(input("Enter angle for left ear (0 to 180): "))  
   servoAngle(leftEar, angle)  
   angle2 \= int(input("Enter angle for right ear (0 to 180): "))  
   servoAngle(rightEar, angle2)
```

`servoAngle()` is the core function for controlling the ears. It takes in a servo object and a target angle, then moves the servo to that angle. You will call this function from `robotFunctions.py` later to move the ears in response to face detection.

`servoRun()` is a test function used to manually verify that both ear servos are working correctly. It prompts you to type in an angle for each ear, then calls `servoAngle()` to move them. This function is only used for testing and will not be called in the final vision script.

5) **Make a call to the `servoRun()` function at the bottom of the script**

`servoRun()`

## **Testing the Program**

1) **Run `python servoMovement.py` in the terminal.** You should see a prompt pop up asking for the angle for the left ear**.**

2) **Input an angle of \-50 and press enter.** Once you give the program an input, it should move the left “ear” from the upright position you set it to in [*Setting Up the Hardware*](https://docs.google.com/document/d/1UGiC80ufGEso83c7PnFgwOVApgB1t09mBcOQ6ye1Nho/edit?tab=t.ogwc9fc1zjum) to be pointed downwards.  
   .  
3) **Do the same for the right ear and input an angle of 20 to get it to the same angle as the left “ear” but mirrored.**

## **Integrating Servo Movement into the Vision**

**At the top of `robotFunctions.py`, import the following:**

```
from gpiozero import AngularServo  
from servoMovement import servoAngle, leftEar, rightEar
```

**Replace the if else block in `robotFunctions.py` with the code below.**

Take notice of the calls to the servoAngle function you defined in servoMovement.py

```
if len(faces) \> 0:

           servoAngle(leftEar, \-90)  
           servoAngle(rightEar, 90)  
           *\# Draw rectangle around first face*  
           x, y, w, h \= faces\[0\]  
           cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  
           cv2.putText(frame, "Face detected\!", (10, 30),  
                      cv2.FONT\_HERSHEY\_SIMPLEX, 1, (0, 255, 0), 2)  
       else:  
           *\# No face \- ears down (sad)*  
           servoAngle(leftEar, \-50)  
           servoAngle(rightEar, 20)  
           cv2.putText(frame, "No face", (10, 30),  
                      cv2.FONT\_HERSHEY\_SIMPLEX, 1, (0, 0, 255), 2)
```

1. **Save the file and then run `python robotFunctions.py` in the terminal.** You should see a small preview screen pop up with the live camera feed.
2. **Point the Raspberry Pi camera towards your face.** In the preview, you should see a box drawn around your face, following your face as you move around in the camera’s view.
3. **Verify the “ears” perk up when the robot sees your face.** Your face should also be boxed on the screen.

The “ear” behavior should look similar to the behavior seen in [this video](https://www.linkedin.com/posts/enricatan_learningbydoing-mvp-studentengineer-ugcPost-7412607119331397633-oUia?utm_source=share&utm_medium=member_desktop&rcm=ACoAADxBaAcBc-s9EvLg0e5CcpeBwrDSlSofJi0).

