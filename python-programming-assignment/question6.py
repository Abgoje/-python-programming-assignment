# question6.py - Loop Examples
# Purpose: Demonstrate for loops and while loops

print("="*50)
print("QUESTION 6 - LOOP EXAMPLES")
print("="*50)

# EXAMPLE 1: For loop with range
print("\nEXAMPLE 1 - For loop (numbers 1 to 10):")
print("-"*50)

for i in range(1, 11):
    print(f"Number: {i}")

# EXAMPLE 2: For loop with list
print("\n" + "="*50)
print("EXAMPLE 2 - For loop (iterate over list):")
print("-"*50)

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# EXAMPLE 3: For loop with index
print("\n" + "="*50)
print("EXAMPLE 3 - For loop (with index):")
print("-"*50)

for index, fruit in enumerate(fruits, 1):
    print(f"{index}. {fruit}")

# EXAMPLE 4: While loop
print("\n" + "="*50)
print("EXAMPLE 4 - While loop (counting down):")
print("-"*50)

count = 5
while count > 0:
    print(f"Countdown: {count}")
    count = count - 1  # Decrease count by 1
print("Blastoff!")

# EXAMPLE 5: Multiplication table
print("\n" + "="*50)
print("EXAMPLE 5 - Nested loop (multiplication table):")
print("-"*50)

print("Multiplication Table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}×{j}={i*j}", end="  ")
    print()  # New line after each row

# EXAMPLE 6: Loop with break and continue
print("\n" + "="*50)
print("EXAMPLE 6 - Break and Continue:")
print("-"*50)

print("Numbers with break (stop at 5):")
for i in range(1, 11):
    if i == 6:
        break  # Exit loop when i equals 6
    print(i, end=" ")
print("\n")

print("Numbers with continue (skip 5):")
for i in range(1, 11):
    if i == 5:
        continue  # Skip this iteration
    print(i, end=" ")
print("\n")

# EXAMPLE 7: Sum using loop
print("\n" + "="*50)
print("EXAMPLE 7 - Calculate sum using loop:")
print("-"*50)

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total = total + num  # Add each number to total

print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# EXAMPLE 8: Loop with user input
print("\n" + "="*50)
print("EXAMPLE 8 - Loop with user input:")
print("-"*50)

user_input = input("Enter 'quit' to exit, or anything else to continue: ")
attempts = 0

while user_input.lower() != 'quit':
    attempts += 1
    print(f"Attempt {attempts}: You entered: {user_input}")
    user_input = input("Enter 'quit' to exit, or anything else to continue: ")

print(f"Total attempts: {attempts}")

print("\n" + "="*50)
print("Program complete!")
print("="*50)
