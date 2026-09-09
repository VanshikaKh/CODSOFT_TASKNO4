# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Display the available operations
print("\nChoose an operation:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

# Ask the user to choose an operation
operation = input("Enter the operation (+, -, *, /): ")

# Check which operation the user selected
if operation == "+":

    # Add the two numbers
    result = num1 + num2
    print("Result:", result)

elif operation == "-":

    # Subtract the second number from the first
    result = num1 - num2
    print("Result:", result)
elif operation == "*":

    # Multiply the two numbers
    result = num1 * num2
    print("Result:", result)
elif operation == "/":

    # Check if the second number is zero
    if num2 == 0:
        print("Error! Cannot divide by zero.")

    else:
        # Divide the first number by the second number
        result = num1 / num2
        print("Result:", result)
else:

    # Display an error for an invalid operation
    print("Invalid operation!")