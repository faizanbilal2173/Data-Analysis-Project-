# Error Handling Practice (Try and Except)

try:
    # Agar user integer ki jagah text likhega toh except block chalega
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
    print("Error: Please enter numbers only (Integers)!")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
