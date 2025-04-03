# Project 6: Countdown Timer Python Project
import time;


def countdown(t):
   while t > 0:
      mins, secs = divmod(t, 60)
      hours, mins = divmod(mins, 60)
      print(f"\r{hours:02d}:{mins:02d}:{secs:02d}",end="")
      time.sleep(1)
      t -= 1
      if t == 0:
         print("\nTime's up!")


input_time = int(input("Enter time in seconds: "))

countdown(input_time) 

