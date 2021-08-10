import time
import sys

string = input("Enter a string to be written in the typing effect: ")

if len(string) < 1:
    string = "Hello World, I am a Python Program being typed out in the typewriter effect!"

userInputspeed = input("Enter the speed of the typing effect: ")

if len(userInputspeed) < 1:
    userInputspeed = 0.05

try:
    speed = float(userInputspeed)
except:
    raise Exception("Please enter a valid number (it can be a decimal number)")

for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(speed)