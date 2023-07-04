0x09. Python - Everything is object :snake:
This repository contains the solutions for the project "0x09. Python - Everything is object" in the ALX Higher Level Programming curriculum.

##Project Details

Language: Python
Topic: OOP
Author: Guillaume
Weight: 1
Start Date: Jul 4, 2023 6:00 AM
Deadline: Jul 5, 2023 6:00 AM
Checker Release: Jul 4, 2023 12:00 PM
Auto Review: A review will be launched at the deadline.
Background Context
In this project, we delve deeper into understanding how Python works with different types of objects. We explore concepts like object mutability, variable assignment, reference, aliasing, and more. The project includes questions that test your understanding of Python's specificity and its handling of different object types.

Make sure to read the documentation, think critically, and discuss with your peers before attempting the questions. Avoid solely relying on the Python interpreter for answers. This project will help you grasp the reasons behind Python's behavior and prepare you for similar questions in Python interviews.

##Resources

To successfully complete this project, you may need to refer to the following resources:
9.10. Objects and values
9.11. Aliasing
Immutable vs mutable types
Mutation (Only this chapter)
9.12. Cloning lists
Python tuples: immutable but potentially changing
Learning Objectives
By the end of this project, you should be able to explain the following concepts without the help of external resources:

Why Python programming is awesome
What is an object
The difference between a class, an object, and an instance
The difference between immutable and mutable objects
The concept of reference and variable assignment
Understanding aliases and identifying identical variables
Displaying the variable identifier (memory address in CPython)
Understanding mutability and immutability
Built-in mutable and immutable types
How Python passes variables to functions

##Requirements

Python Scripts
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All files should end with a newline character
The first line of all script files should be exactly #!/usr/bin/python3
A README.md file is mandatory at the root of the project folder
Your code should follow the PEP 8 style (version 2.8.*) and use the pycodestyle linter
All files must be executable
The length of your files will be tested using wc
.txt Answer Files
Only one line
No Shebang
All files should end with a newline character
Project Tasks

##The project includes the following tasks: :page_with_curl:

**Task 0: Who am I?**
Write the function id that returns the unique ID of an object in the file 1-answer.txt. The function should have the following prototype: def id(obj):.

**Task 2: Right count**
Write the function def count() -> int: that returns the number of instances of a class. The function should have the following prototype: def count() -> int:.

**Task 3: Same or not?**
Write the function is_same_class(obj, a_class) that checks if an object is an instance of a specified class. The function should have the following prototype: def is_same_class(obj, a_class):.

**Task 4: Only sub class of**
Write the function def inherits_from(obj, a_class) that checks if an object is an instance of a class that inherited (directly or indirectly) from a specified class. The function should have the following prototype: def inherits_from(obj, a_class):.

**Task 5: Geometry module**
Write an empty class BaseGeometry in the file 5-base_geometry.py. This class will serve as the base class for future geometric shapes.

**Task 6: Improve Geometry**
Write a class BaseGeometry (based on 5-base_geometry.py) with public instance methods area(self) and integer_validator(self, name, value). The integer_validator method should raise an exception with a specified message if the value is not an integer.

**Task 7: Integer validator**
Write a class BaseGeometry (based on 6-base_geometry.py) with a public instance method integer_validator(self, name, value) that validates the value.

**Task 8: Rectangle**
Write a class Rectangle that inherits from BaseGeometry (based on 7-base_geometry.py). The Rectangle class should have a constructor that initializes the width and height attributes.

**Task 9: Full rectangle**
Write a class Rectangle that inherits from BaseGeometry (based on 8-base_geometry.py). The Rectangle class should have a constructor that initializes the width and height attributes. It should also have a __str__ method that returns a string representation of the rectangle.

**Task 10: Square #1**
Write a class Square that inherits from Rectangle (based on 9-rectangle.py). The Square class should have a constructor that initializes the size attribute.

**Task 11: Square #2**
Write a class Square that inherits from Rectangle (based on 10-square.py). The Square class should have a constructor that initializes the size attribute. The size attribute should be validated using the integer_validator method from the BaseGeometry class.

**Task 12: My integer**
Write a class MyInt that inherits from int. Invert the behavior of the == and != operators for instances of MyInt and int.

**Task 13: Can I?**
Write a function add_attribute(obj, attribute, value) that adds a new attribute to an object if it's possible. If it's not possible, raise a TypeError with the message "can't add new attribute".

**Task 14: Pascal's Triangle**
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal's triangle of n. Each value in the triangle should be the result of summing the two values directly above it.


