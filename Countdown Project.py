# Here, the user is required to input a number between 1 and 500 and the programs uses it as the start value for the countdown

# We use the time module to control the speed of the countdown
# We use the pyinputplus module to ensure that users input the expected value

import time
import pyinputplus as pyip

# This code collects the value (Integer) from user
t = pyip.inputNum("Enter number: ", lessThan=500)

# this function accepts the user input and starts the countdown


def countdown(m):
    while m:
        mins, secs = divmod(m, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        m -= 1
    print("Timer Completed")


countdown(t)
