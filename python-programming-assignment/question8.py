# question8.py - Lists and Tuples
# Purpose: Learn about lists and tuples data structures

print("="*50)
print("QUESTION 8 - LISTS AND TUPLES")
print("="*50)

# SECTION 1: Lists
print("\n" + "="*50)
print("LISTS - Mutable collections")
print("="*50)

# Creating a list
fruits = ["Apple", "Banana", "Orange", "Mango"]
print(f"\nOriginal list: {fruits}")

# Accessing list elements
print(f"First element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")
print(f"Elements from index 1 to 3: {fruits[1:3]}")

# Modifying list elements
fruits[0] = "Strawberry"
print(f"After changing first element: {fruits}")

# Adding elements
fruits.append("Grapes")
print(f"After append('Grapes'): {fruits}")

fruits.insert(2, "Pineapple")
print(f"After insert at index 2: {fruits}")

# Removing elements
fruits.remove("Banana")
print(f"After remove('Banana'): {fruits}")

last_fruit = fruits.pop()
print(f"After pop(): {fruits}")
print(f"Removed element: {last_fruit}")

# List operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nNumber list: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Count of 1s: {numbers.count(1)}")
print(f"Index of 5: {numbers.index(5)}")

# Sorting list
numbers_sorted = sorted(numbers)
print(f"Sorted: {numbers_sorted}")
print(f"Sorted reverse: {sorted(numbers, reverse=True)}")

# List comprehension
squared = [x**2 for x in range(1, 6)]
print(f"Squared numbers (1-5): {squared}")

even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers from list: {even_numbers}")

# Looping through list
print("\nLooping through fruits:")
for index, fruit in enumerate(fruits):
    print(f"  {index + 1}. {fruit}")

# SECTION 2: Tuples
print("\n" + "="*50)
print("TUPLES - Immutable collections")
print("="*50)

# Creating a tuple
colors = ("Red", "Green", "Blue", "Yellow")
print(f"\nOriginal tuple: {colors}")

# Accessing tuple elements
print(f"First color: {colors[0]}")
print(f"Last color: {colors[-1]}")
print(f"Colors from index 1 to 3: {colors[1:3]}")

# Tuple properties
print(f"Length: {len(colors)}")
print(f"Count of 'Red': {colors.count('Red')}")
print(f"Index of 'Blue': {colors.index('Blue')}")

# Tuples are immutable - this will cause error if uncommented:
# colors[0] = "Orange"  # TypeError: 'tuple' object does not support item assignment

# Converting between list and tuple
color_list = list(colors)
print(f"\nConverted to list: {color_list}")
color_tuple = tuple(color_list)
print(f"Converted back to tuple: {color_tuple}")

# Tuple packing and unpacking
print("\nTuple packing and unpacking:")
person = ("Alice", 25, "Engineer")
name, age, profession = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")

# Multiple return values (returns tuple)
def get_coordinates():
    return (10, 20, 30)

x, y, z = get_coordinates()
print(f"\nCoordinates - x: {x}, y: {y}, z: {z}")

# Single element tuple (note the comma)
single_tuple = (42,)
print(f"\nSingle element tuple: {single_tuple}")
print(f"Type: {type(single_tuple)}")

# Comparing lists and tuples
print("\n" + "="*50)
print("LISTS vs TUPLES")
print("="*50)

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print(f"List: {my_list}")
print(f"Tuple: {my_tuple}")
print(f"\nList is mutable: Can be changed")
print(f"Tuple is immutable: Cannot be changed")
print(f"List uses square brackets: []")
print(f"Tuple uses parentheses: ()")

# Performance consideration
import sys
print(f"\nList size in memory: {sys.getsizeof(my_list)} bytes")
print(f"Tuple size in memory: {sys.getsizeof(my_tuple)} bytes")

print("\n" + "="*50)
print("Program complete!")
print("="*50)
