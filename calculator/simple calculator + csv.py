# This is a simple calculator
# This script saves the history of the calculation in a csv file


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


def express(num1, num2, operator, result):
    expressionn = f"{num1} {operator} {num2} = "
    print(expressionn, result)
    rows.append([expressionn, result])


def calc(w, num1, num2):
    if w == 1:
        operator = "+"
        result = addition(num1, num2)
        express(num1, num2, operator, result)

    elif w == 2:
        operator = "-"
        result = subtraction(num1, num2)
        express(num1, num2, operator, result)

    elif w == 3:
        operator = "*"
        result = multiplication(num1, num2)
        express(num1, num2, operator, result)

    else:
        operator = "/"
        result = division(num1, num2)
        express(num1, num2, operator, result)


def user_input():
    userInput = pyip.inputInt(
        prompt="1: Addition \n2: Subtraction \n3: Multiplication \n4: Division", lessThan=5)

    num1 = pyip.inputInt("Input the first number")
    num2 = pyip.inputInt("Input the second number")
    calc(userInput, num1, num2)


user_input()
do_more()

with open("Calc Result.csv", "w", newline="") as calculation:
    # Create a writer object
    write_csv = csv.writer(calculation)

    # write the fields
    write_csv.writerow(field)

    # write the rows
    write_csv.writerows(rows)
