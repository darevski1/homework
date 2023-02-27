# Wellcome message
message = print(
    "This is simple calculator written in Python. Please please choose operator"
)
# Dictionary are used to store data values in key:value pairs.
operator = {
    "1": "Add",
    "2": "subtract",
    "3": "multiply",
    "4": "divide ",
}
# This is for loop in Dictionary where we get key:pair value
for x, y in operator.items():
    print(x, y)

# Get user value from input

# define function to accept user input and validate input
 
def userInput():
    userOperator = int(input("Enter number:"))
    getValue = type(userOperator)
    if getValue == int:
        print ("Integer")
    else:
        exit
        
ccc = userInput()
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
    match userOperator:
        case (1):
            print(numberOne, "+", numberOne, "=", int(add(numberOne, numberOne)))
        case (2):
            print(numberOne, "-", numberOne, "=", subtract(numberOne, numberOne))
        case (3):
            print(numberOne, "*", numberOne, "=", multiply(numberOne, numberOne))
        case (4):
            print(numberOne, "/", numberOne, "=", divide(numberOne, numberOne))


# aacpted values from user input

 
listNumber = [1, 2, 3, 4]
 
if ccc in listNumber:
    numberOne = float(input("Enter first Number: "))
    numberTwo = float(input("Enter second Number: "))
    # calling calculator function
    calculator()
else:
    checkInput = int(
        input(
            "Invalid input, plaase choose number from 1 - 4.  \n To try again press (1), or press any key to close: "
        )
    )
    if checkInput == 1:
        userOperator = int(
            input(
                "Enter your number: \n (1) to add, \n (2) to subtract, \n (3) to multiply, \n (4) to devide. \n Number:  "
            )
        )
        numberOne = float(input("Enter Number: "))
        numberTwo = float(input("Enter Number: "))

        calculator()
    else:
        exit
