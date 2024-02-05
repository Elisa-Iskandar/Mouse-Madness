import ctypes 
import random 
import threading
import keyboard 

SPI_GETMOUSESPEED = 0x0070
SPI_SETMOUSESPEED = 0x0071
speedlevels = 10 

running = False
originalsens = ctypes.windll.user32.SystemParametersInfoA(SPI_GETMOUSESPEED, 1, None, 0)

def setsens():
   sens = random.randint(0, speedlevels - 1)
   ctypes.windll.user32.SystemParametersInfoA(SPI_SETMOUSESPEED, 0, sens, 0)
   print("sens changed")

def restoresens():
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETMOUSESPEED, 0, originalsens, 0)
    print("sens restored")

def toggle():
    global running
    if running:
        restoresens()
        running = False
        print("off")
    else:
        randominterval()
        running = True
        print("on")

keyboard.add_hotkey("F3", toggle)

def randominterval():
   while True:
       setsens()
       interval = random.randint(0,5)
       threading.Timer(interval, randominterval).start() 

if __name__ == "__main__":
    keyboard.wait()
