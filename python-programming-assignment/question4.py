# question4.py - Even or Odd Checker
# Purpose: Use if-else conditions to determine if a number is even or odd

print("="*50)
print("QUESTION 4 - EVEN OR ODD CHECKER")
print("="*50)

# Take input from user
number = int(input("\nEnter a number: "))

print("\n" + "="*50)
print("RESULT:")
print("="*50)

# Check if number is even or odd
# Even numbers are divisible by 2 (remainder = 0)
# Odd numbers have remainder 1 when divided by 2

if number % 2 == 0:
    print(f"{number} is an EVEN number")
    print(f"Explanation: {number} ÷ 2 = {number // 2} with remainder 0")
else:
    print(f"{number} is an ODD number")
    print(f"Explanation: {number} ÷ 2 = {number // 2} with remainder 1")

# Additional information
print("\n" + "="*50)
print("ADDITIONAL INFORMATION:")
print("="*50)

# Check if positive or negative
if number > 0:
    print(f"The number {number} is POSITIVE")
elif number < 0:
    print(f"The number {number} is NEGATIVE")
else:
    print(f"The number is ZERO")

# Check if single or multi-digit
if abs(number) < 10:
    print(f"{number} is a SINGLE-DIGIT number")
else:
    num_digits = len(str(abs(number)))
    print(f"{number} is a {num_digits}-DIGIT number")

print("\n" + "="*50)
print("Program complete!")
print("="*50)
