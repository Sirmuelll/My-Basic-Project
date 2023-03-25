# This is a calculator program
# Road Map
# - Create The Frame of the Calculator
# - Use the mainloop function to keep control of the activities in the calculator
# - Create the text field
# - Create the buttons

# import the neccessary module
from tkinter import *
import csv
import datetime

# Setting all parameters related to the frame/window of the calculator
window = Tk()  # initialize the tkinter module
window.configure(bg="#b38600")  # defining the background color of the window
window.title("Calculator")  # The title of the calculator
window.geometry("350x465")  # The dimension of our calculator frame
# window.iconbitmap('calcu.png')
window.resizable(False, False)

# Create the text field
# This creates a frame within the window
button_frame = Frame(window, bg="#b38600")
button_frame.pack()  # This code helps in the display of the text field, but we need an entry box to finally dispay the field

# this variable "equation" is assigned to a StringVar() so that we can retrieve text from inside it and pass the variable to our textvariable parameter for a widget like "Entry"
equation = StringVar()
# Our text_field variable takes a method called Entry which accepts the button frame and textvariable, that allows us to grab whatever is inside the box
text_field = Entry(button_frame, textvariable=equation,
                   font=("arial", 30, "bold"), width=17, bg="#c49c21")


# defining the functions
expression = ''
result = ''
calculation_history = []  # This stores the history of our calculations


# def history():
#     if x == []:
#         equation.set("There is no history yet")
#     else:
#         for i in x:
#             equation.set("*i")


def press(num):
    global expression

    expression += str(num)
    equation.set(expression)
    print(expression)


def equalpress():
    global expression
    global calculation_history

    try:
        global result

        result = str(eval(expression))
        equation.set(result)
        full_expression = f"{expression} = {result}"
        calculation_history.append(full_expression)
        expression = ''
        print(calculation_history)

        # # We need to create a CSV file to store the history data of the calculations
        with open("calculator.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            # d = datetime.datetime.now()
            writer.writerow(["Expression"])
            writer.writerow(calculation_history)
        csv_file.close()
    except:
        equation.set("error")
        expression = ''


def clear():
    global expression

    expression = ""
    equation.set("0")


def anss():
    global result
    global expression

    equation.set(result)
    expression += result


def dell():
    global expression

    expression = expression[:-1]
    equation.set(expression)


# creating the buttons
button7 = Button(button_frame, text="7", font=("Times new roman", 12), relief="ridge",
                 borderwidth=2, bg="#ffdf80", width=8, height=4, command=lambda: press(7))
button8 = Button(button_frame, text="8", font=("Times new roman", 12), relief="ridge",
                 borderwidth=2, bg="#ffdf80", width=8, height=4, command=lambda: press(8))
button9 = Button(button_frame, text="9", font=("Times new roman", 12), relief="ridge",
                 borderwidth=2, bg="#ffdf80", width=8, height=4, command=lambda: press(9))
delkey = Button(button_frame, text="del", font=("Times new roman", 12), relief="ridge",
                borderwidth=2, bg="#806000", width=8, height=4, command=dell)
button4 = Button(button_frame, text="4", font=("Times new roman", 12), relief="ridge",
                 borderwidth=2, bg="#ffdf80", width=8, height=4, command=lambda: press(4))
button5 = Button(button_frame, text="5", font=("Times new roman", 12), relief="ridge",
                 borderwidth=2, bg="#ffdf80", width=8, height=4, command=lambda: press(5))
button6 = Button(button_frame, text="6", font=("Times new roman", 12), relief="ridge",
                 borderwidth=2, bg="#ffdf80", width=8, height=4, command=lambda: press(6))
addition = Button(button_frame, text="+", font=("Times new roman", 12), relief="ridge",
                  borderwidth=2, bg="#806000", width=8, height=4, command=lambda: press("+"))
button1 = Button(button_frame, text="1", font=("Times new roman", 12), relief="ridge",
                 borderwidth=2, bg="#ffdf80", width=8, height=4, command=lambda: press(1))
button2 = Button(button_frame, text="2", font=("Times new roman", 12), relief="ridge",
                 borderwidth=2, bg="#ffdf80", width=8, height=4, command=lambda: press(2))
button3 = Button(button_frame, text="3", font=("Times new roman", 12), relief="ridge",
                 borderwidth=2, bg="#ffdf80", width=8, height=4, command=lambda: press(3))
subtraction = Button(button_frame, text="-", font=("Times new roman", 12), relief="ridge",
                     borderwidth=2, bg="#806000", width=8, height=4, command=lambda: press("-"))
dot = Button(button_frame, text=".", font=("Times new roman", 12), relief="ridge",
             borderwidth=2, bg="#ffdf80", width=8, height=4, command=lambda: press("."))
button0 = Button(button_frame, text="0", font=("Times new roman", 12), relief="ridge",
                 borderwidth=2, bg="#ffdf80", width=8, height=4, command=lambda: press(0))
cancel = Button(button_frame, text="C", font=("Times new roman", 12),
                relief="ridge", borderwidth=2, bg="#ffdf80", width=8, height=4, command=clear)
division = Button(button_frame, text="/", font=("Times new roman", 12), relief="ridge",
                  borderwidth=2, bg="#806000", width=8, height=4, command=lambda: press("/"))

equals = Button(button_frame, text="=", font=("Times new roman", 12), relief="ridge",
                borderwidth=2, bg="#ffdf80", width=8, height=4, command=equalpress)
answer = Button(button_frame, text="ans", font=("Times new roman", 12),
                relief="ridge", borderwidth=2, bg="#ffdf80", width=8, height=4, command=anss)
multiplication = Button(button_frame, text="x", font=("Times new roman", 12), relief="ridge",
                        borderwidth=2, bg="#806000", width=8, height=4, command=lambda: press("*"))


# These displays all of our codes (text_field and buttons) using the grid() function
text_field.grid(row=0, column=0, columnspan=4, ipadx=17, ipady=20, pady=15)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
delkey.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
addition.grid(row=2, column=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
subtraction.grid(row=3, column=3)

dot.grid(row=4, column=0)
button0.grid(row=4, column=1)
cancel.grid(row=4, column=2)
division.grid(row=4, column=3)

equals.grid(row=5, column=0, columnspan=2, rowspan=3, sticky="we")
answer.grid(row=5, column=2)
multiplication.grid(row=5, column=3)


window.mainloop()  # keeps the window active until the closed button is pressed
