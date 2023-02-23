message = print("This is simple calculator written in Python. Please choose operator")


# function addition of two numbers
def add(x, y):
    return x + y


# divide two numbers
def subtract(x, y):
    return x - y


# divide two numbers
def multiply(x, y):
    return x * y


# divide two numbers
def divide(x, y):
    return x / y


# calculator function
def calculator():
    if userinput == 1:
        print(numberOne, "+", numberOne, "=", int(add(numberOne, numberOne)))
    elif userinput == 2:
        print(numberOne, "-", numberOne, "=", int(subtract(numberOne, numberOne)))
    elif userinput == 3:
        print(numberOne, "*", numberOne, "=", int(multiply(numberOne, numberOne)))
    elif userinput == 4:
        print(numberOne, "/", numberOne, "=", int(divide(numberOne, numberOne)))


while True:
    userinput = int(
        input(
            "Enter your number: \n (1) to add, \n (2) to subtract, \n (3) to multiply, \n (4) to devide. \n Number:  "
        )
    )
    if userinput == 1 or userinput == 2 or userinput == 3 or userinput == 4:
        numberOne = int(input("Enter Number: "))
        numberTwo = int(input("Enter Number: "))
        calculator()
    else:
        continue

    getAnswer = input("Would you like to make another calculation type yes / no ")
    if getAnswer == "yes":
        continue
    elif getAnswer == "no":
        break
