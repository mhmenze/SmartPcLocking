# Smart PC Locking and Pausing Assistant

This is a Human Computer Interaction project that makes use of an Arduino Microcontroller, along with an Ultrasound sensor to carry out the following activities automatically:

1)If the user leaves the computer, automatically lock it to prevent unauthorized access.

2)If the user is watching a video/movie and leaves the PC, then instead of locking the video will be paused.

3)While the user is in front of the computer for extended periods of time, display a popup reminder to take a break.

## How it works:

-Ultrasound Sensor measures the distance of the user and sends the readings to the Arduino microcontroller.

-Arduino microcontroller connects with the PC over USB serial connection.

-Python scripts accesses the serial port, and reads the values from the US sensor. Considering the distance reading, and checking if a video is playing or not, the necessary action is carried out by the python script (Locking or Pausing). Further, the python script also tracks time since it was run and sends a popup reminder to rest.

**This was designed and tested only for Windows OS.

## Requirements:

-Arduino Uno R3 board

-Ultrasound Sensor HC-SR04

## Instructions

-Upload the .ino file code to the Arduino UNO board.

-Run the app.py script in your pc while the device is connected via USB.
