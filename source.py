# Example python file with multiple deliberate issues for static analysis testing

import os
import sys

# Unused import
import time

# Global variable - poor practice for mutable types
global_list = []

def calcualtion(a, b):  # Misspelled function name
    # Unused variable
    result = a + b

    # Possible semantic error (should it return the result?)
    print("This function adds two numbers.")

def unused_function():
    # This function is never used
    pass

# Mutable default argument - can lead to unexpected behavior
def add_to_list(value, list_to_add_to=[]):
    list_to_add_to.append(value)
    print(list_to_add_to)

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Inconsistent usage of underscore for 'private' variable

    # No self argument - this will raise an error
    def get_details():
        return f"Name: {self.name}, Age: {self._age}"

# Insecure use of input
user_input = input("Enter your command: ")
os.system(user_input)  # Potential security risk

# Syntax error: missing parentheses
print "This will not print"

# Equality comparison with single '='
if user_input = 'exit':
    sys.exit()

# Correct style but potential bug - might be meant to be 'is not None'
if user_input is not None:
    print("You entered:", user_input)

# Infinite recursive function - no base case
def recursive_function():
    recursive_function()

# Call function with too many arguments
calcualtion(1, 2, 3)

# Call function with missing arguments
calcualtion()

# Catching Exception is too broad
try:
    risky_operation()
except Exception as e:
    pass  # Bare except and pass - poor exception handling

# Using 'global' keyword unnecessarily
def set_global_value():
    global global_list
    global_list = [1, 2, 3]

# Function defined after use
def risky_operation():
    undefined_variable / 0  # ZeroDivisionError

# Call function defined later in the code
risky_operation()

# Assigning a lambda to a name, not the best practice
add = lambda x, y: x + y

# Executing a string with eval is a security risk
eval('os.system("ls")')

# Rebind a built-in function
list = 'I am not a list now'

# This is the end of the file with issues for static analysis
