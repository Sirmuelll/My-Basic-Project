import pyinputplus as pyip
import csv

field = ["Expression", "Result"]
rows = []


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def do_more():
    while True:
        more_calc = pyip.inputYesNo("wanna do more calculations?").lower()
        if more_calc == "yes":
            user_input()
        else:
            break


def calc(w, num1, num2):
    if w == 1:
        print(f"{num1} + {num2} = {addition(num1, num2)}")
    elif w == 2:
        print(f"{num1} - {num2} = {subtraction(num1, num2)}")
    elif w == 3:
        print(f"{num1} x {num2} = {multiplication(num1, num2)}")
    else:
        print(f"{num1} / {num2} = {division(num1, num2)}")


def user_input():
    userInput = pyip.inputInt(
        prompt="1: Addition \n2: Subtraction \n3: Multiplication \n4: Division", lessThan=5)

    num1 = pyip.inputInt("Input the first number")
    num2 = pyip.inputInt("Input the second number")
    calc(userInput, num1, num2)


user_input()
do_more()
