# question10.py - File Handling
# Purpose: Learn how to read, write, and manage files

import os

print("="*50)
print("QUESTION 10 - FILE HANDLING")
print("="*50)

# SECTION 1: Writing to a file
print("\n" + "="*50)
print("SECTION 1 - Writing to Files")
print("="*50)

# Create and write to a file
print("\nCreating 'sample.txt' file...")
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a Python file handling example.\n")
    file.write("Python is amazing!\n")

print("File created successfully!")

# Writing multiple lines
print("\nCreating 'numbers.txt' file...")
with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"Number: {i}\n")

print("Numbers file created!")

# SECTION 2: Reading from a file
print("\n" + "="*50)
print("SECTION 2 - Reading from Files")
print("="*50)

# Method 1: Read entire file at once
print("\nMethod 1 - read() - Read entire file:")
print("-"*50)
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Method 2: Read line by line
print("Method 2 - readlines() - Read all lines as list:")
print("-"*50)
with open("sample.txt", "r") as file:
    lines = file.readlines()
    for index, line in enumerate(lines, 1):
        print(f"Line {index}: {line.strip()}")

# Method 3: Read file line by line in loop
print("\nMethod 3 - Loop through file:")
print("-"*50)
with open("sample.txt", "r") as file:
    for line in file:
        print(f"Read: {line.rstrip()}")

# SECTION 3: Appending to a file
print("\n" + "="*50)
print("SECTION 3 - Appending to Files")
print("="*50)

print("\nAppending to 'sample.txt'...")
with open("sample.txt", "a") as file:
    file.write("This line was appended!\n")
    file.write("Appending does not erase existing content.\n")

print("Content appended!")

# Display updated file
print("\nUpdated file content:")
with open("sample.txt", "r") as file:
    print(file.read())

# SECTION 4: File operations and methods
print("\n" + "="*50)
print("SECTION 4 - File Operations")
print("="*50)

# Check if file exists
print(f"\nFile 'sample.txt' exists: {os.path.exists('sample.txt')}")
print(f"File 'nonexistent.txt' exists: {os.path.exists('nonexistent.txt')}")

# Get file size
file_size = os.path.getsize("sample.txt")
print(f"File size: {file_size} bytes")

# Get file name
print(f"File name: {os.path.basename('sample.txt')}")

# Get file directory
print(f"Directory: {os.path.dirname('sample.txt') or 'Current directory'}")

# SECTION 5: Working with different file modes
print("\n" + "="*50)
print("SECTION 5 - File Modes")
print("="*50)

print("\nFile modes:")
print("  'r'  - Read (default)")
print("  'w'  - Write (creates new file)")
print("  'a'  - Append")
print("  'x'  - Create (fails if exists)")
print("  'rb' - Read binary")
print("  'wb' - Write binary")

# SECTION 6: Creating a student records file
print("\n" + "="*50)
print("SECTION 6 - Practical Example: Student Records")
print("="*50)

# Create student records
print("\nCreating student records file...")
with open("students.txt", "w") as file:
    file.write("Name,Age,GPA\n")
    file.write("John,20,3.85\n")
    file.write("Jane,21,3.92\n")
    file.write("Bob,20,3.75\n")
    file.write("Alice,21,3.88\n")

print("Student records created!")

# Read and display student records
print("\nStudent Records:")
print("-"*50)
with open("students.txt", "r") as file:
    for line in file:
        print(line.rstrip())

# SECTION 7: Parsing CSV-like data
print("\n" + "="*50)
print("SECTION 7 - Parsing File Data")
print("="*50)

print("\nParsing student data:")
with open("students.txt", "r") as file:
    header = file.readline().strip().split(",")
    print(f"Columns: {header}")
    
    print("\nStudent Details:")
    for line in file:
        data = line.strip().split(",")
        name, age, gpa = data
        print(f"  {name}: Age={age}, GPA={gpa}")

# SECTION 8: Error handling with files
print("\n" + "="*50)
print("SECTION 8 - Error Handling")
print("="*50)

# Try to read a file that might not exist
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("\n[ERROR] File not found!")
    print("The file 'missing_file.txt' does not exist.")

# SECTION 9: File operations with paths
print("\n" + "="*50)
print("SECTION 9 - File Path Operations")
print("="*50)

# List all files in current directory
print("\nFiles in current directory:")
files = os.listdir(".")
python_files = [f for f in files if f.endswith(".py")]
text_files = [f for f in files if f.endswith(".txt")]

if python_files:
    print(f"  Python files: {python_files}")
if text_files:
    print(f"  Text files: {text_files}")

# SECTION 10: Cleanup
print("\n" + "="*50)
print("SECTION 10 - File Cleanup")
print("="*50)

# Delete temporary files (commented out to keep for review)
print("\nTemporary files created:")
print("  - sample.txt")
print("  - numbers.txt")
print("  - students.txt")
print("\nTo delete these files, use: os.remove('filename')")
print("Uncomment the code below to delete:")
print("# os.remove('sample.txt')")
print("# os.remove('numbers.txt')")
print("# os.remove('students.txt')")

print("\n" + "="*50)
print("Program complete!")
print("="*50)
