import ctypes 
import random 
import threading
import keyboard 

SPI_SETMOUSESPEED = 0x0070 
SPEED_LEVELS = 10 

def setsens():
   sens = random.randint(0, SPEED_LEVELS - 1)
   ctypes.windll.user32.SystemParametersInfoA(SPI_SETMOUSESPEED, 0, sens, 0)

def runtimer():
   while True:
       setsens()
       timer = threading.Timer(5, setsens) 
       timer.start()
       if keyboard.is_pressed("esc"):  
           print("Program stopped.")
           break  

if __name__ == "__main__":
    runtimer()
