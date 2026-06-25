# Simple Calculator Program

# User se inputs lena
val1 = int(input("Enter your first value: "))
val2 = int(input("Enter your second value: "))
operator = input("Enter operator (+, -, *, /): ")

# Operations check karna
if operator == "+":
    print("Your answer is:", val1 + val2)
elif operator == "-":
    print("Your answer is:", val1 - val2)
elif operator == "*":
    print("Your answer is:", val1 * val2)
elif operator == "/":
    # Zero division error se bachne ke liye chota sa check
    if val2 != 0:
        print("Your answer is:", val1 / val2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid Operator!")
