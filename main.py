import time
import sys

string = input("Enter a string to be written in the typing effect: ")
speed = float(input("Enter the speed of the typing effect: "))

for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)