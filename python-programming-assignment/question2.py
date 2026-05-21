# question2.py - Variables and User Input
# Purpose: Learn about variables, data types, and taking input from users

print("="*50)
print("QUESTION 2 - VARIABLES AND USER INPUT")
print("="*50)

# Taking input from the user
print("\nPlease enter your information:")

# Input function reads user input as a string
name = input("Enter your name: ")
age = input("Enter your age: ")

# Converting string to integer for age
age = int(age)

# Creating variables of different types
height = float(input("Enter your height (in cm): "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

# Displaying the collected information
print("\n" + "="*50)
print("INFORMATION COLLECTED:")
print("="*50)
print(f"Name: {name}")
print(f"Age: {age} years")
print(f"Height: {height} cm")
print(f"Student: {is_student}")

# Calculating next year age
next_year_age = age + 1
print(f"\nNext year you will be: {next_year_age} years old")

# Demonstrating variable types
print("\n" + "="*50)
print("DATA TYPES:")
print("="*50)
print(f"Type of name: {type(name)}")        # Should be <class 'str'>
print(f"Type of age: {type(age)}")          # Should be <class 'int'>
print(f"Type of height: {type(height)}")    # Should be <class 'float'>
print(f"Type of is_student: {type(is_student)}")  # Should be <class 'bool'>

print("\n" + "="*50)
print("Program complete!")
print("="*50)
