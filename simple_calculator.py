# Custom functions for arithmetic operations
def d(a, b):
    sum = a + b
    return sum

def s(a, b):
    subtraction = a - b
    return subtraction

def m(a, b):
    multiplication = a * b
    return multiplication

def di(a, b):
    division = a / b
    return division

# Prompting user to select an arithmetic operator
print("Choose Your Operation : + , - , * , /")
choose = input("What do you Want to do with Numbers ? = ")

# Capturing operands from the user
x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))

# Conditional execution based on selected operation
if choose == "+":
    print("Sum is : ", d(x, y))
elif choose == "-":
    print("Subtraction is : ", s(x, y))
elif choose == "*":
    print("Multiplication is : ", m(x, y))
elif choose == "/":
    print("Division is : ", di(x, y))
else:
    print("Plz use the correct operation !")
