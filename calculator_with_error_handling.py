# Arithmetic Calculator with Exception Handling

try:
    # Capturing input values and converting to integers
    val1 = int(input("Enter your first value: "))
    val2 = int(input("Enter your second value: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print("Your answer is:", val1 + val2)
    elif operator == "-":
        print("Your answer is:", val1 - val2)
    elif operator == "*":
        print("Your answer is:", val1 * val2)
    elif operator == "/":
        print("Your answer is:", val1 / val2)
    else:
        print("Invalid Operator!")

except ValueError:
    # Handles cases where user inputs text instead of integers
    print("Error: Please enter numbers only (Integers)!")
except ZeroDivisionError:
    # Handles runtime division by zero error
    print("Error: Division by zero is not allowed!")
except Exception as e:
    # Catch-all block for any other unexpected runtime exceptions
    print(f"An unexpected error occurred: {e}")
