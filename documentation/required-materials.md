# **Required Materials**

This document contains references to all the materials required to create this project.

| Table of Contents | Related Documents |
|---|---|
| [Hardware](#hardware) | [Building a Creature-like, Face-Detection Robot Using Raspberry Pi (Home Page)](README.md) |
| [Software](#software) | [Setting up the Hardware](hardware-set-up.md) |
| | [Setting up the Raspberry Pi and the Raspberry Pi Camera](rasp-pi-set-up.md) |
| | [Setting up the Robot's Vision](robot-vision.md) |
| | [Setting up the "Ear Motors"](ear-motors.md) |
| | [Frequently Answered Questions](faq.md) |

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
| 3D Printed Parts |  | [CAD Files](https://drive.google.com/drive/u/0/folders/1kP5vw27MX55-eW444j8cTzyY8JGihCrh) | Able to be printed in PLA (cheapest 3D printing material) Also working to create online kits  containing these 3D parts you can purchase in case you don’t have access to a printer |
| Small Phillips-head Screwdriver |  |  |  |


### **Software**

| Software / Package | Terminal Command(s) | Notes |
| :---- | :---- | :---- |
| Raspberry Pi 5 OS (64-bit) |  | Download using [Raspberry Pi Imager](https://www.raspberrypi.com/software/) |
| VSCode | `sudo apt update` `sudo apt install code`  | [Tutorial](https://code.visualstudio.com/docs/setup/raspberry-pi) for VSCode download |
| OpenCV (cv2) | `pip install opencv-python -break-system-packages` |  |
| Picamera2 | `sudo apt install -y python3-picamera2` |  |
| gpiozero | `sudo apt install -y python3-gpiozero` |  |

