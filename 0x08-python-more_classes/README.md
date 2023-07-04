0x08. Python - More Classes and Objects
This project contains solutions for various tasks related to object-oriented programming (OOP) in Python. It covers topics such as classes, objects, attributes, methods, data abstraction, data encapsulation, information hiding, properties, class attributes, class methods, static methods, and more.

Learning Objectives
By completing this project, you should be able to:

Explain the awesomeness of Python programming
Understand the concepts of object-oriented programming (OOP)
Grasp the idea of "first-class everything"
Define a class and create objects/instances
Differentiate between a class and an object/instance
Understand attributes and their types (public, protected, private)
Use the self parameter in class methods
Implement the special __init__ method for object initialization
Understand data abstraction, data encapsulation, and information hiding
Define properties and differentiate them from attributes
Use the __str__ and __repr__ methods for string representation of objects
Differentiate between __str__ and __repr__
Understand class attributes and their scope
Differentiate between object attributes and class attributes
Implement class methods and static methods
Dynamically create new attributes for existing instances of a class
Bind attributes to objects and classes
Understand and utilize the __dict__ attribute of a class and an instance of a class
Understand how Python finds the attributes of an object or class
Use the getattr function to retrieve attributes
Requirements
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
All files should end with a new line
The first line of all files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder, is mandatory
Code should use the pycodestyle (version 2.8.*)
All files must be executable
The length of your files will be tested using wc
Tasks
0. Simple rectangle
Define an empty class Rectangle that represents a rectangle. No additional functionality is required.

1. Real definition of a rectangle
Define a class Rectangle that represents a rectangle with the following specifications:

Private instance attribute: width:
Property def width(self): to retrieve the width
Property setter def width(self, value): to set the width
The width must be an integer. Otherwise, raise a TypeError exception with the message "width must be an integer".
If the width is less than 0, raise a ValueError exception with the message "width must be >= 0".
Private instance attribute: height:
Property def height(self): to retrieve the height
Property setter def height(self, value): to set the height
The height must be an integer. Otherwise, raise a TypeError exception with the message "height must be an integer".
If the height is less than 0, raise a ValueError exception with the message "height must be >= 0".
Instantiation with optional width and height: def __init__(self, width=0, height=0).
2. Area and Perimeter
Update the class Rectangle with the following additional functionality:

Public instance method: def area(self): returns the area of the rectangle.
Public instance method: `def perimeter(self)  with cutoff at 2021-09-06

3. String representation
Update the class Rectangle with the following additional functionality:

Override the __str__ method to return a string representation of the rectangle in the format [Rectangle] <width>/<height>.
4. Eval is magic
Update the class Rectangle with the following additional functionality:

Override the __repr__ method to return a string representation of the rectangle in the format Rectangle(<width>, <height>).
5. Detect instance deletion
Update the class Rectangle with the following additional functionality:

Print the message "Bye rectangle..." when an instance of Rectangle is deleted.
6. How many instances
Update the class Rectangle with the following additional functionality:

Add a class attribute number_of_instances and initialize it to 0.
Increment the number_of_instances attribute by 1 whenever a new instance is created.
Decrement the number_of_instances attribute by 1 whenever an instance is deleted.
7. Change representation
Update the class Rectangle with the following additional functionality:

Add a class attribute print_symbol and initialize it to #.
Override the __str__ method to return a string representation of the rectangle using the print_symbol attribute.
8. Compare rectangles
Update the class Rectangle with the following additional functionality:

Add a class method def bigger_or_equal(rect_1, rect_2): returns the rectangle with the greater area or rect_1 if both rectangles have the same area.
The method should take two Rectangle instances as arguments and return the instance with the greater area. If either of the rectangles is not an instance of the Rectangle class, the method should raise a TypeError exception with the message "rect_1 must be an instance of Rectangle" or "rect_2 must be an instance of Rectangle".
9. A square is a rectangle
Define a class Square that inherits from the class Rectangle. The Square class should have the same attributes and methods as the Rectangle class.
