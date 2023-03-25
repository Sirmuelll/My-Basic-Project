import random
import time
import pyinputplus as pyip

print("Welcome to your password generator")
time.sleep(1)

input1 = pyip.inputNum("Input the NUMBER of passwords you want to generate: ")
input2 = pyip.inputNum("Input the LENGTH of password you want: ")

dictionary = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_=+[]\<>"

time.sleep(1)
storage = []
for x in range(input1):
    generator = ""
    # print(generator)
    for d in range(input2):
        # print(d)
        generator += random.choice(dictionary)
    storage.append(generator)
    # print(generator)
    time.sleep(0.3)
print(storage)
