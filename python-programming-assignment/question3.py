# question3.py - Arithmetic Calculator
# Purpose: Perform mathematical operations on user input

print("="*50)
print("QUESTION 3 - ARITHMETIC CALCULATOR")
print("="*50)

# Take input from user
print("\nEnter two numbers for calculation:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display menu
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%) - Remainder")
print("6. Exponentiation (**) - Power")

choice = input("\nEnter your choice (1-6): ")

# Perform calculation based on choice
print("\n" + "="*50)
print("CALCULATION RESULT:")
print("="*50)

if choice == '1':
    result = num1 + num2
    operation = "Addition"
    symbol = "+"
elif choice == '2':
    result = num1 - num2
    operation = "Subtraction"
    symbol = "-"
elif choice == '3':
    result = num1 * num2
    operation = "Multiplication"
    symbol = "*"
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        operation = "Division"
        symbol = "/"
    else:
        print("[ERROR] Cannot divide by zero!")
        result = None
        operation = None
elif choice == '5':
    if num2 != 0:
        result = num1 % num2
        operation = "Modulus"
        symbol = "%"
    else:
        print("[ERROR] Cannot perform modulus with zero!")
        result = None
        operation = None
elif choice == '6':
    result = num1 ** num2
    operation = "Exponentiation"
    symbol = "**"
else:
    print("[ERROR] Invalid choice!")
    result = None
    operation = None

# Display result
if result is not None:
    print(f"Operation: {operation}")
    print(f"Expression: {num1} {symbol} {num2}")
    print(f"Result: {result}")
else:
    print("Calculation could not be performed.")

print("\n" + "="*50)
print("Program complete!")
print("="*50)
