# **Frequently Answered Questions**

| Table of Contents | Related Documents |
|---|---|
| [What can the robot do?](#what-can-the-robot-do) | [Building a Creature-like, Face-Detection Robot Using Raspberry Pi (Home Page)](README.md) |
| [Can the robot identify who a face belongs to?](#can-the-robot-identify-who-a-face-belongs-to) | [Required Materials](required-materials.md) |
| [Does the robot work in low light?](#does-the-robot-work-in-low-light) | [Setting up the Hardware](hardware-set-up.md) |
| [Can the robot detect faces through glasses or a mask?](#can-the-robot-detect-faces-through-glasses-or-a-mask) | [Setting up the Raspberry Pi and the Raspberry Pi Camera](rasp-pi-set-up.md) |
| [Why can't the robot detect faces from the side?](#why-cant-the-robot-detect-faces-from-the-side) | [Setting up the Robot's Vision](robot-vision.md) |
| [Can I change the angle the “ear” servos move to?](#can-i-change-the-angle-the-ear-servos-move-to) | [Setting Up the “Ear” Motors](ear-motors.md) |
| [Why is the camera feed slow or laggy?](#why-is-the-camera-feed-slow-or-laggy) | |
| [Why do the ears jitter or twitch when nothing is happening?](#why-do-the-ears-jitter-or-twitch-when-nothing-is-happening) | |
| [Can I use a different servo, camera, or Raspberry Pi model for this project?](#can-i-use-a-different-servo-camera-or-raspberry-pi-model-for-this-project) | |

## **What can the robot do?**

The robot can:

* Detect human faces in real-time using the camera feed  
* Distinguish between when a face is present or not present  
* Indicate whether it detects a face with servo movements  
* Operate continuously while powered on

---

## **Can the robot identify who a face belongs to?**

No. The classifier used is a pre-trained model that you imported in [Setting Up the Robot's Vision](?tab=t.qxdwur558bl6). It can only detect whether a face is present in the frame. If you want the robot to recognize specific people, you would need to use a face recognition library and train it on labeled images of the people you want it to identify.

---

## **Does the robot work in low light?**

It can, but may display unreliable performance. The Haar cascade face detection model, the pre-trained model this project uses, relies on the contrast between light and shadow to identify face-shaped patterns in the live camera feed. Detection becomes less reliable in dim lighting and may fail entirely in dark conditions. For the best results, make sure the person’s face is well-lit from the front.

---

## **Can the robot detect faces through glasses or a mask?**

Glasses should not interfere with face detection, though masks probably will. Glasses generally do not interfere with detection because most of the face’s contour can still be seen. Masks that cover the nose and mouth significantly reduce accuracy because the Haar cascade face detection model was trained on unobstructed front-facing human faces. This means that when key facial features are hidden, the model may not classify the highlights and shadows from the mask as being similar enough to those of a human’s face.

---

## **Why can't the robot detect faces from the side?**

The model it uses wasn’t trained to identify side profiles. The Haar cascade classifier used in this project was trained specifically on front-facing faces. It learned to recognize the pattern of the eyes, nose, and mouth as they appear when someone is looking straight at the camera. A face turned to the side looks very different from that pattern, so the model won't recognize it. If you need profile detection, you would need a separate classifier trained on human side-profiles.

---

## **Can I change the angle the “ear” servos move to?**

Yes. The angles the ears move to are set by the values passed to servoAngle( ) in robotFunctions.py. You can adjust these freely within the SG90's supported range of −90° to 90°. To test different angles and find one you like before committing to them in the main script, run servoMovement.py in the terminal. It will prompt you to enter angles for each ear and will move them in real time.

---

## **Why is the camera feed slow or laggy?**

The Raspberry Pi processes the camera feed frame by frame, running face detection on every single frame. With needing to process several frames per second, this process can be intense for a Raspberry Pi, which has lower specifications than the average laptop. If you experience lag, try reducing the resolution the camera captures at (the default is 640×480 pixels). 

---

## **Why do the ears jitter or twitch when nothing is happening?**

Jitter is usually caused by electrical noise passing through the servo signal wire, which happens because electricity doesn’t flow smoothly. Smaller electronics are especially susceptible to noise. Jitter due to noise can be mitigated by adding small 220 - 470 ohm resistors, which help dampen the noise passing through to the signal wire.

---

## **Can I use a different servo, camera, or Raspberry Pi model for this project?**

This project hasn't been tested with a different setup, but hypothetically yes, though there may be some incompatibilities. Software-wise, this guide is specifically written for the Raspberry Pi 5 and its OS, so some terminal commands used in the tutorials may not work on earlier Pi models. If you use a different servo model, you will likely need to adjust the min\_pulse\_width and max\_pulse\_width values in servoMovement.py specified under [Setting Up the “Ear” Motors](?tab=t.7dpg6n5ri98z) to match your servo's specification sheet. If you use a different camera or an earlier Pi model, you will need to make sure the ribbon cable you purchase is compatible with both devices. Using a different servo model may render the 3D printed parts incompatible if the servo dimensions or screw holes are different.
