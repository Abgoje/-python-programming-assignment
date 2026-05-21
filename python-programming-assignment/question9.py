# question9.py - Dictionary Usage
# Purpose: Learn about dictionaries (key-value pairs)

print("="*50)
print("QUESTION 9 - DICTIONARY USAGE")
print("="*50)

# SECTION 1: Creating and accessing dictionaries
print("\n" + "="*50)
print("SECTION 1 - Creating Dictionaries")
print("="*50)

# Method 1: Using curly braces
student = {
    "name": "John Doe",
    "age": 20,
    "gpa": 3.85,
    "major": "Computer Science"
}

print(f"\nStudent dictionary: {student}")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"GPA: {student['gpa']}")

# Method 2: Using dict() constructor
person = dict(name="Alice", age=25, city="New York")
print(f"\nPerson dictionary: {person}")

# SECTION 2: Dictionary operations
print("\n" + "="*50)
print("SECTION 2 - Dictionary Operations")
print("="*50)

# Adding new key-value pairs
student["email"] = "john@university.edu"
print(f"\nAfter adding email: {student}")

# Modifying existing values
student["gpa"] = 3.90
print(f"After updating GPA: {student}")

# Removing items
del student["major"]
print(f"After removing major: {student}")

# Using pop() method
removed_age = student.pop("age")
print(f"Removed age: {removed_age}")
print(f"Dictionary after pop: {student}")

# SECTION 3: Accessing dictionary data
print("\n" + "="*50)
print("SECTION 3 - Accessing Dictionary Data")
print("="*50)

info = {
    "name": "Bob",
    "age": 30,
    "country": "USA",
    "job": "Developer"
}

# Using get() method (safer - returns None if key doesn't exist)
print(f"\nUsing get() method:")
print(f"Name: {info.get('name')}")
print(f"Salary: {info.get('salary')}")  # Returns None
print(f"Salary with default: {info.get('salary', 'Not specified')}")

# Check if key exists
print(f"\nKey 'name' exists: {'name' in info}")
print(f"Key 'salary' exists: {'salary' in info}")

# Get all keys, values, and items
print(f"\nAll keys: {list(info.keys())}")
print(f"All values: {list(info.values())}")
print(f"All items: {list(info.items())}")

# SECTION 4: Looping through dictionary
print("\n" + "="*50)
print("SECTION 4 - Looping Through Dictionary")
print("="*50)

print("\nLooping through keys:")
for key in info:
    print(f"  {key}")

print("\nLooping through values:")
for value in info.values():
    print(f"  {value}")

print("\nLooping through items (key-value pairs):")
for key, value in info.items():
    print(f"  {key}: {value}")

# SECTION 5: Dictionary methods
print("\n" + "="*50)
print("SECTION 5 - Dictionary Methods")
print("="*50)

print(f"\nOriginal: {info}")

# Update with another dictionary
new_info = {"age": 31, "city": "Boston"}
info.update(new_info)
print(f"After update: {info}")

# Clear all items
copy_info = info.copy()
copy_info.clear()
print(f"After clear: {copy_info}")

# SECTION 6: Nested dictionaries
print("\n" + "="*50)
print("SECTION 6 - Nested Dictionaries")
print("="*50)

company = {
    "name": "TechCorp",
    "employees": {
        "emp1": {"name": "John", "position": "Manager"},
        "emp2": {"name": "Jane", "position": "Developer"},
        "emp3": {"name": "Bob", "position": "Designer"}
    },
    "location": "San Francisco"
}

print(f"\nCompany: {company['name']}")
print(f"Location: {company['location']}")
print(f"\nEmployees:")
for emp_id, emp_info in company["employees"].items():
    print(f"  {emp_id}: {emp_info['name']} - {emp_info['position']}")

# SECTION 7: Dictionary with lists as values
print("\n" + "="*50)
print("SECTION 7 - Dictionary with Lists")
print("="*50)

grades = {
    "John": [85, 90, 88],
    "Jane": [92, 95, 89],
    "Bob": [78, 80, 82]
}

print("\nStudent Grades:")
for student_name, scores in grades.items():
    average = sum(scores) / len(scores)
    print(f"  {student_name}: {scores} (Average: {average:.2f})")

# SECTION 8: Practical example - Phone book
print("\n" + "="*50)
print("SECTION 8 - Practical Example: Phone Book")
print("="*50)

phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

print("\nPhonebook:")
for name, phone in phone_book.items():
    print(f"  {name}: {phone}")

# Search in phone book
search_name = input("\nEnter a name to search: ")
if search_name in phone_book:
    print(f"Phone number: {phone_book[search_name]}")
else:
    print("Contact not found")

print("\n" + "="*50)
print("Program complete!")
print("="*50)
