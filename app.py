import serial
import os
import time
import tkinter as tk
from tkinter import messagebox
import pyautogui
import psutil

ser = serial.Serial('COM3', 9600)       # Change the port name and baud rate as needed

root = tk.Tk()                          # Create the Tk() object only once
root.title("Smart PC Proximity Lock")
#root.withdraw()
root.geometry("400x480")

def start():
    runStatus = True
    check_proximity(runStatus)

def stop():
    runStatus = False
    check_proximity(runStatus)

def inputRest():
    global restTime
    restTime = int(restWarningTime.get())*60
    print(restTime)

def inputDistance():
    global distanceVal
    distanceVal = int(lockingDistance.get())
    print(distanceVal)

def check_proximity(x):
    reset_timer()

    videoStatus = "playing"
    # Check if VLC media player is running
    vlc_running = False
    for proc in psutil.process_iter():
        if "vlc" in proc.name().lower():
            vlc_running = True
            break
    while x:

        line = ser.readline().decode().strip() # Read a line from the serial port and decode it
        print(line)

        # Convert the line variable to an integer
        try:
            line = int(line)
        except: 
            line = 400  #Max range of US sensor
            continue

        if line > distanceVal :
            if vlc_running and videoStatus =="playing":

                # Get the VLC media player window
                app = pyautogui.getWindowsWithTitle('VLC media player')[0]

                # Activate the VLC window
                app.activate()

                # Pause the video by pressing the spacebar key
                pyautogui.press('space')

                videoStatus = "paused"
            elif not vlc_running:
                # Lock the computer if VLC media player is not running
                os.system("rundll32.exe user32.dll,LockWorkStation")

            reset_timer()
            while True:
                if not x:
                    break
                line = ser.readline().decode().strip() # Read a line from the serial port and decode it
                # Convert the line variable to an integer
                try:
                    line = int(line)
                except: 
                    line = 400  #Max range of US sensor
                    continue
                
                if line < distanceVal:
                    reset_timer()
                    break
                #time.sleep(0.1)
        else:
            if vlc_running and videoStatus == "paused":
                # Get the VLC media player window
                app = pyautogui.getWindowsWithTitle('VLC media player')[0]

                # Activate the VLC window
                app.activate()

                # Play the video by pressing the spacebar key
                pyautogui.press('space')

                videoStatus = "playing"

            check_timer()
            
        if not x:
            break

restLabel = tk.Label(text = "\n\nEnter Rest reminder time in minutes")
restWarningTime = tk.Entry()
restTimeButton = tk.Button(text="Done", command = inputRest)
restLabel.pack()
restWarningTime.pack(pady = 10)
restTimeButton.pack()

space1 = tk.Label(text = "\n" )
space1.pack()

distanceLabel = tk.Label(text = "Enter Distance to Lock in cm")
lockingDistance = tk.Entry()
distanceButton = tk.Button(text="Done", command = inputDistance)
distanceLabel.pack()
lockingDistance.pack(pady = 10)
distanceButton.pack()

space2 = tk.Label(text = "\n" )
space2.pack()

startButton = tk.Button(text="Start", command = start)
startButton.pack(pady = 20)

copyRightLabel = tk.Label(text = "\nUniversity of Sri Jayawardenapura\nHuman Computer Interacction\n2023\n© A Project by M.Nazeer and Sithira", fg='#808080',)
copyRightLabel.pack()

def reset_timer():
    global start_time
    start_time = time.time()

def check_timer():
    global root                         # Access the global Tk() object

    elapsed_time = time.time() - start_time
    if elapsed_time >= restTime:
        print("Take a rest")
        message = 'Take a rest'
        title = 'Rest Reminder'
        messagebox.showinfo(title, message)
        reset_timer()

root.mainloop()