# **Required Materials**

This document contains references to all the materials required to create this project.

| Table of Contents | Related Documents |
|---|---|
| [Hardware](#hardware) | [Building a Creature-like, Face-Detection Robot Using Raspberry Pi (Home Page)](../README.md) |
| [Software](#software) | [Setting up the Hardware](hardware-set-up.md) |
| | [Setting up the Raspberry Pi and the Raspberry Pi Camera](rasp-pi-set-up.md) |
| | [Setting up the Robot's Vision](robot-vision.md) |
| | [Setting up the "Ear Motors"](ear-motors.md) |
| | [Frequently Asked Questions](faq.md) |

### **Hardware**

| Material Name | Specific Model / Requirements  (if applicable) | Link I Purchased From | Notes |
| :---- | :---- | :---- | :---- |
| Raspberry Pi | Raspberry Pi 5 | [Amazon](https://www.amazon.com/dp/B0CRSNCJ6Y?ref=ppx_yo2ov_dt_b_fed_asin_title%20) | 8GB RAM version or higher recommended  |
| MicroSD | 32 GB |  | 32 GB or higher recommended **Included in the linked Raspberry Pi kit** |
| USB-C Power Cable and Brick | 27 W \- 45 W |  | **Included in the linked Raspberry Pi kit** |
| Powered display monitor  | Has HDMI input |  |  |
| Micro-USB to HDMI cable |  |  | **Included in the linked Raspberry Pi kit** |
| Raspberry Pi Camera  | Camera Module 3 | [Amazon](https://www.amazon.com/dp/B0BX6N6V98?ref=ppx_yo2ov_dt_b_fed_asin_title%20) |  |
| Ribbon Cable | Ribbon Cable for Raspberry Pi 5 |  | **Included with the linked Raspberry Pi Camera** |
| USB Mouse | USB-A |  | Bluetooth pairing is possible, but is more complicated to set up |
| USB Keyboard | USB-A |  | Bluetooth pairing is possible |
| Servos | SG90  | [Amazon](https://www.amazon.com/dp/B09GFN98X9?ref=ppx_yo2ov_dt_b_fed_asin_title%20) |  |
| Jumper Wires | Male-to-female Male-to-male |  | **Male-to-female wires included with the linked servos** |
| Power Module | HiLetGo | [Amazon](https://www.amazon.com/HiLetgo-Supply-Module-Prototype-Breadboard/dp/B00HJ6AE72/ref=sr_1_1?crid=1L4FWGGZMJ23F&dib=eyJ2IjoiMSJ9.46eVfNcBm7aKmhRLu1BFwFUIZ2jeHgjWwVNDAwbe38w4R_K1S1x4P24a_ne5xiKZbY-QfPzri54A_5q-m5fmNy6A3KpwsiVqRQEPzoBbxOeXFOJdSHRUOi49eEw4XnFXxLD_UQx5YvH_GCnoQBTbzWqkMDvwlo6ay8EYelh-8l5r5uZd5McdVyrD30ME6FAtG2Cw6HXXBQ1kuc5QY7gpRjDWGhnoAYTNssAMxlGbL3o.P2B1r40QjuFdwTuQZo0kQKPav9D2JAYW7RE-clE0HK0&dib_tag=se&keywords=Power%2BModules%2Bhiletgo&qid=1772438153&sprefix=power%2Bmodules%2Bhiletgo%2Caps%2C163&sr=8-1&th=1) |  |
| Barrel Jack Power Cable and Brick | 2.1mm |  |  |
| Breadboard |  | [Amazon](https://www.amazon.com/DIYables-Half-Size-Breadboard-Arduino-Raspberry/dp/B0BXKM8DQ8/ref=sr_1_30?crid=FJILDTB663PW&dib=eyJ2IjoiMSJ9.x1VJ5zp8OPAxySBS0mN9QpslpQnXhT1N6bF1ex3-PN3YuoiGNAR4oxtplaXh8IMc7wSNLCvwBJDaX-o9G5pPi0GnL2qAt1s2bh21vpm4FSnIwEip6MmBJjKtfPrKYHmeXdXidygvSC9RrYwiIRIi7ZDHXCo8vikH5ipFpinmaTF8K-j1A2xFxZRwEOnehjCCPkD5EgP2lYzg02WPAkzyvZUqXP4rGLKN1aiBCSfkPOrHFuYF2fR_nrJCN7TVtLYHaxHMT5BWhFKPW0uoRwRciu-lhnYxu95DlQgI6UNTVhg.v-TntBQdV1OISx8nECjqhGjzFCrzVHIhm4qRL_L13eM&dib_tag=se&keywords=breadboard&qid=1772353378&s=electronics&sprefix=breadboar%2Celectronics%2C174&sr=1-30&th=1) |  |
| 3D Printed Parts |  | [CAD Files](https://cad.onshape.com/documents/89cd369ef21127fd7299b2b1/w/98cd03dbaca4f82dab6a6156/e/31e971ed38c5ba3b7745d6cc) | Able to be printed in PLA (cheapest 3D printing material) |
| Small Phillips-head Screwdriver |  |  |  |
| Servo Driver | PCA9685 | [Amazon](https://www.amazon.com/Teyleten-Robot-PCA9685-Compatible-Raspberry/dp/B0CNVBWX2M/ref=sr_1_1?dib=eyJ2IjoiMSJ9.os3aVLN8-3BtpzxM7kRBbjqCWDrk4ijBwLQ34TwEMJ8Nw0jmwGKH4WxLsC9wNgV2t-YyoWECiN_784-lwKhXdHkcR8Gn6XMBg3SZha2WWoTk7il3KmE_In8hj0_9k61tGwJ1n8lX1s_by3VdQtwXf8mWUcBGbCb3ol4VCANZmSl67teJqw7-dY8L4zzbbyA-sFwfJ1dQ_5O7B8ziSu-nXZ3dg69pXABywqtLoqu9oGUk09qiaG88azDBUhhRjwvGfvD0aVTi6xUKCDLNh5bamIQ1tvNF1Kn5DacFUgXjQ9Q.ej7YSuY1KmVB5kaI3JU-BhS5vv3nHRdnWiuCDIfFu3o&dib_tag=se&keywords=Teyleten+Robot+PCA9685+16+Channel+12+bit+PWM+Servo+Motor+Driver+I2C+IIC+Module+for+MG90S+SG90+MG995+Compatible+with+Arduino+Raspberry+Pi+%282pcs%29&nsdOptOutParam=true&qid=1785979398&s=electronics&sr=1-1) |  |


### **Software**

| Software / Package | Terminal Command(s) | Notes |
| :---- | :---- | :---- |
| Raspberry Pi 5 OS (64-bit) |  | Download using [Raspberry Pi Imager](https://www.raspberrypi.com/software/) |
| VSCode | `sudo apt update` `sudo apt install code`  | [Tutorial](https://code.visualstudio.com/docs/setup/raspberry-pi) for VSCode download |
| OpenCV (cv2) | `pip install opencv-python -break-system-packages` |  |
| Picamera2 | `sudo apt install -y python3-picamera2` |  |
| Adafruit Servo-Kit | `sudo apt install -y python3-adafruit-circuitpython-servokit -break-system-packages` |  |

