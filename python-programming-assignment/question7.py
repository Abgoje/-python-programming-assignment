# question7.py - Functions
# Purpose: Learn how to create and use functions

print("="*50)
print("QUESTION 7 - FUNCTIONS")
print("="*50)

# FUNCTION 1: Simple function with no parameters
def greet():
    """Function that prints a greeting message"""
    print("Hello! Welcome to Python Functions!")

print("\nFunction 1 - Simple greeting:")
print("-"*50)
greet()

# FUNCTION 2: Function with parameters
def add(a, b):
    """Function that adds two numbers"""
    sum_result = a + b
    return sum_result

print("\n" + "="*50)
print("Function 2 - Addition:")
print("-"*50)
result = add(5, 3)
print(f"add(5, 3) = {result}")

# FUNCTION 3: Function with multiple parameters
def calculate_area(length, width):
    """Function that calculates rectangle area"""
    area = length * width
    return area

print("\n" + "="*50)
print("Function 3 - Calculate Area:")
print("-"*50)
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = calculate_area(length, width)
print(f"Area of rectangle: {area}")

# FUNCTION 4: Function with default parameters
def power(base, exponent=2):
    """Function with default parameter (exponent defaults to 2)"""
    result = base ** exponent
    return result

print("\n" + "="*50)
print("Function 4 - Power function:")
print("-"*50)
print(f"power(5) = {power(5)}")          # Uses default exponent=2
print(f"power(5, 3) = {power(5, 3)}")    # Specifies exponent=3

# FUNCTION 5: Function returning multiple values
def get_student_info(name, math, english, science):
    """Calculate average and determine grade"""
    total = math + english + science
    average = total / 3
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "F"
    
    return average, grade

print("\n" + "="*50)
print("Function 5 - Student Grading:")
print("-"*50)
avg, grade = get_student_info("John", 85, 90, 88)
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")

# FUNCTION 6: Function that modifies a list
def add_to_list(my_list, value):
    """Add a value to a list"""
    my_list.append(value)
    return my_list

print("\n" + "="*50)
print("Function 6 - List manipulation:")
print("-"*50)
my_numbers = [1, 2, 3, 4, 5]
print(f"Original list: {my_numbers}")
my_numbers = add_to_list(my_numbers, 6)
print(f"After adding 6: {my_numbers}")

# FUNCTION 7: Factorial function (recursion)
def factorial(n):
    """Calculate factorial of a number"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print("\n" + "="*50)
print("Function 7 - Factorial (Recursion):")
print("-"*50)
num = 5
fact = factorial(num)
print(f"Factorial of {num} = {fact}")

# FUNCTION 8: Function with loops
def print_table(number, limit=10):
    """Print multiplication table"""
    print(f"Multiplication table of {number}:")
    for i in range(1, limit + 1):
        print(f"{number} × {i} = {number * i}")

print("\n" + "="*50)
print("Function 8 - Multiplication Table:")
print("-"*50)
print_table(7, 5)

# FUNCTION 9: Checking if number is prime
def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

print("\n" + "="*50)
print("Function 9 - Prime Number Checker:")
print("-"*50)
test_numbers = [2, 5, 10, 11, 15, 17]
for num in test_numbers:
    if is_prime(num):
        print(f"{num} is PRIME")
    else:
        print(f"{num} is NOT PRIME")

# FUNCTION 10: Function documentation
def divide(a, b):
    """
    Divide two numbers safely.
    
    Args:
        a: Dividend (number to be divided)
        b: Divisor (number to divide by)
    
    Returns:
        Result of division or None if division by zero
    """
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    return a / b

print("\n" + "="*50)
print("Function 10 - Documented function:")
print("-"*50)
print(divide.__doc__)  # Print function documentation
print(f"divide(10, 2) = {divide(10, 2)}")

print("\n" + "="*50)
print("Program complete!")
print("="*50)
