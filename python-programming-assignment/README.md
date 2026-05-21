# Python Programming Assignment

A comprehensive collection of beginner-to-intermediate Python programming exercises covering fundamental concepts and practical applications.

## 📋 Assignment Overview

This assignment contains 10 complete Python programs that cover essential programming concepts. Each question is in a separate file with full comments and explanations.

## 📁 Project Structure

```
python-programming-assignment/
│
├── question1.py      # Hello World
├── question2.py      # Variables and User Input
├── question3.py      # Arithmetic Calculator
├── question4.py      # Even or Odd Checker
├── question5.py      # Largest Number Finder
├── question6.py      # Loop Examples
├── question7.py      # Functions
├── question8.py      # Lists and Tuples
├── question9.py      # Dictionary Usage
├── question10.py     # File Handling
└── README.md         # This file
```

## 📚 Questions Breakdown

### Question 1 - Hello World
**Purpose**: Introduction to Python output
**Concepts**:
- Print statements
- String output
- Escape sequences

**Run**: `python question1.py`

---

### Question 2 - Variables and User Input
**Purpose**: Learn about variables, data types, and user input
**Concepts**:
- Variable declaration
- Data types (int, float, string, bool)
- User input with input()
- Type conversion
- F-strings for formatting

**Run**: `python question2.py`
**Interactive**: Yes - requires user input

---

### Question 3 - Arithmetic Calculator
**Purpose**: Perform mathematical operations
**Concepts**:
- Arithmetic operators (+, -, *, /, %, **)
- Conditional statements (if-elif-else)
- User choice handling
- Error handling for division by zero

**Run**: `python question3.py`
**Interactive**: Yes - requires user input

---

### Question 4 - Even or Odd Checker
**Purpose**: Use conditions to analyze numbers
**Concepts**:
- Modulus operator (%)
- If-else conditions
- String methods
- Number properties

**Run**: `python question4.py`
**Interactive**: Yes - requires user input

---

### Question 5 - Largest Number Finder
**Purpose**: Find maximum value among numbers
**Concepts**:
- Comparison operators
- Multiple approaches (if-elif, max() function, loops)
- List operations
- Sorting

**Run**: `python question5.py`
**Interactive**: Yes - requires user input

---

### Question 6 - Loop Examples
**Purpose**: Understand for and while loops
**Concepts**:
- For loops with range()
- List iteration
- While loops
- Nested loops
- Break and continue statements
- Loop with user input

**Run**: `python question6.py`
**Interactive**: Yes - includes interactive loop

---

### Question 7 - Functions
**Purpose**: Learn function definition and usage
**Concepts**:
- Function definition
- Parameters and arguments
- Return values
- Default parameters
- Recursion
- Function documentation

**Run**: `python question7.py`

---

### Question 8 - Lists and Tuples
**Purpose**: Work with list and tuple data structures
**Concepts**:
- List creation and modification
- List methods (append, remove, pop, sort)
- List slicing
- List comprehension
- Tuples and immutability
- Tuple unpacking
- List vs Tuple comparison

**Run**: `python question8.py`
**Interactive**: No

---

### Question 9 - Dictionary Usage
**Purpose**: Work with key-value pair structures
**Concepts**:
- Dictionary creation
- Accessing values
- Adding and modifying items
- Dictionary methods (keys, values, items, get)
- Nested dictionaries
- Looping through dictionaries
- Practical applications

**Run**: `python question9.py`
**Interactive**: Yes - includes search functionality

---

### Question 10 - File Handling
**Purpose**: Read, write, and manage files
**Concepts**:
- File modes (r, w, a)
- Context manager (with statement)
- Reading files (read, readlines, line-by-line)
- Writing and appending
- File operations (exists, size, path)
- Error handling
- CSV-like data parsing

**Run**: `python question10.py`
**Interactive**: No - creates sample files

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Text editor or IDE
- Terminal/Command Prompt

### Running Individual Programs

```bash
# Run any individual program
python question1.py
python question2.py
python question3.py
# ... and so on
```

### Running All Programs (Automated)

```bash
# Create a script to run all programs
for i in {1..10}; do
  echo "Running question$i.py..."
  python question$i.py
done
```

## 📝 Code Features

All programs include:
- ✅ Complete, runnable code
- ✅ Detailed comments explaining each section
- ✅ Beginner-friendly explanations
- ✅ Multiple approaches where applicable
- ✅ Error handling
- ✅ Formatted output
- ✅ Examples and demonstrations

## 💻 Learning Outcomes

After completing this assignment, you will understand:
1. ✓ Basic Python syntax and structure
2. ✓ Variables and data types
3. ✓ Conditional statements (if-elif-else)
4. ✓ Loops (for and while)
5. ✓ Functions and their usage
6. ✓ Lists and list operations
7. ✓ Tuples and immutability
8. ✓ Dictionaries and key-value pairs
9. ✓ File input/output operations
10. ✓ Best practices and code organization

## 🔧 Customization & Enhancement

### Easy Modifications

**Question 1**: Change greeting messages
```python
print("Your custom message here!")
```

**Question 2**: Add more data types (lists, etc.)
```python
hobbies = input("Enter your hobbies: ").split(", ")
```

**Question 3**: Add more operations (square root, etc.)
```python
import math
result = math.sqrt(num1)
```

**Question 6**: Change loop ranges and limits
```python
for i in range(1, 20):  # Change 20 to any number
```

## 🐛 Common Issues & Solutions

**Issue**: "Name 'variable' is not defined"
- **Cause**: Variable used before assignment
- **Solution**: Ensure variable is created before using it

**Issue**: "invalid literal for int()"
- **Cause**: User input is not a valid number
- **Solution**: Add input validation

**Issue**: "FileNotFoundError"
- **Cause**: File doesn't exist or wrong path
- **Solution**: Check file path and ensure file exists

**Issue**: "ZeroDivisionError"
- **Cause**: Division by zero
- **Solution**: Add check for zero before dividing

## 📊 Complexity Levels

- **Beginner**: Questions 1-3
- **Intermediate**: Questions 4-7
- **Advanced**: Questions 8-10

## 📚 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [W3Schools Python](https://www.w3schools.com/python/)
- [Python for Everybody](https://www.py4e.com/)

## 📋 Submission Checklist

Before submitting:
- ✓ All 10 question files are present
- ✓ Code runs without errors
- ✓ Comments are clear and complete
- ✓ Variable names are meaningful
- ✓ Output formatting is consistent
- ✓ README is updated
- ✓ .gitignore is configured
- ✓ Files are organized properly

## 🔐 Best Practices Applied

1. **Comments**: Every major section has comments
2. **Naming**: Clear, descriptive variable names
3. **Organization**: Logical code flow
4. **Error Handling**: Try-except blocks where appropriate
5. **Output Formatting**: Consistent, readable output
6. **Documentation**: Functions include docstrings
7. **DRY Principle**: Avoid code repetition

## 📱 Testing Your Code

### Manual Testing

```bash
# Test each question
python question1.py    # Verify output
python question2.py    # Try different inputs
python question3.py    # Test edge cases
# ... continue for all
```

### Creating Test Cases

For interactive programs, test with:
- Normal inputs
- Edge cases (0, negative numbers, very large numbers)
- Invalid inputs (non-numeric when numeric expected)
- Boundary values

## 🎓 University Submission

### Files to Include

✅ Include:
- All 10 `.py` files
- `README.md` this file
- `.gitignore` file

### ZIP Creation

**Windows**:
```bash
Compress-Archive -Path python-programming-assignment -DestinationPath python-assignment.zip
```

**macOS/Linux**:
```bash
zip -r python-assignment.zip python-programming-assignment
```

### GitHub Upload

```bash
# Initialize git repo
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: Python programming assignment"

# Add remote
git remote add origin https://github.com/yourusername/python-programming-assignment.git

# Push to GitHub
git push -u origin main
```

## 💾 File Size Reference

Total size of all code files: ~1.5 MB
- Fully self-contained
- No external dependencies required
- Ready for submission

## 📞 Support & Questions

If you have questions about any program:
1. Check the comments in the code
2. Review the program description above
3. Test with different inputs
4. Refer to official Python documentation

## ✅ Verification Checklist

```
[ ] All 10 files created and contain code
[ ] Each file runs without errors
[ ] Comments explain the code clearly
[ ] Variable names are meaningful
[ ] Output is properly formatted
[ ] README is complete
[ ] .gitignore is configured
[ ] Ready for submission
```

## 📝 Last Updated

**Created**: 2024
**Status**: Complete and Ready for Submission

---

**Good luck with your Python learning journey!**

For more Python practice, visit:
- HackerRank
- LeetCode
- Codewars
- Project Euler
