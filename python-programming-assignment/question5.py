# question5.py - Find the Largest Number
# Purpose: Use comparison operators to find the maximum number

print("="*50)
print("QUESTION 5 - LARGEST NUMBER FINDER")
print("="*50)

# Method 1: Using three separate variables
print("\nMETHOD 1 - Using three variables:")
print("-"*50)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find the largest using if-elif-else
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"\nNumbers: {num1}, {num2}, {num3}")
print(f"Largest number: {largest}")

# Method 2: Using Python's built-in max() function
print("\n" + "="*50)
print("METHOD 2 - Using max() function:")
print("-"*50)

numbers = [num1, num2, num3]
max_number = max(numbers)
print(f"Using max(): {max_number}")

# Method 3: Using a list and loop (for learning)
print("\n" + "="*50)
print("METHOD 3 - Using loop:")
print("-"*50)

largest_manual = numbers[0]  # Start with first number
for num in numbers:
    if num > largest_manual:
        largest_manual = num  # Update if we find a larger one

print(f"Using loop: {largest_manual}")

# Additional features
print("\n" + "="*50)
print("ADDITIONAL INFORMATION:")
print("="*50)

print(f"Smallest number: {min(numbers)}")
print(f"Sum of numbers: {sum(numbers)}")
print(f"Average of numbers: {sum(numbers) / len(numbers):.2f}")

# Sort numbers
sorted_numbers = sorted(numbers)
print(f"Numbers in ascending order: {sorted_numbers}")
print(f"Numbers in descending order: {sorted(numbers, reverse=True)}")

print("\n" + "="*50)
print("Program complete!")
print("="*50)
