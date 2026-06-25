# Simple Calculator Program for Basic Arithmetic Operations

# Taking inputs from the user
val1 = int(input("Enter your first value: "))
val2 = int(input("Enter your second value: "))
operator = input("Enter operator (+, -, *, /): ")

# Checking operations based on user input
if operator == "+":
    print("Your answer is:", val1 + val2)
elif operator == "-":
    print("Your answer is:", val1 - val2)
elif operator == "*":
    print("Your answer is:", val1 * val2)
elif operator == "/":
    # Prevent application crash by checking for division by zero
    if val2 != 0:
        print("Your answer is:", val1 / val2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid Operator!")
