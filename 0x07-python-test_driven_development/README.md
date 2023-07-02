0x07. Python - Test-driven development

Doctest + unitest in python

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Includes both Holberton-provided ones as well as the
following eight independently-developed:
  * [0-add_integer.txt](./tests/0-add_integer.txt)
  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * [3-say_my_name.txt](./tests/3-say_my_name.txt)
  * [4-print_square.txt](./tests/4-print_square.txt)
  * [5-text_indentation.txt](./tests/text_indentation.txt)
  * [6-max_integer_test.py](./tests/6-max_integer_test.py)

## Function Prototypes:

Prototypes for functions written in this project:

| File                     | Prototype                                    |
| ------------------------ | -------------------------------------------- |
| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |
| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |
| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`      | `def print_square(size):`                    |
| `5-text_indentation.py`  | `def text_indentation(text):`                |

## Tasks :page_with_curl:

* **0. Integers addition**
  * [0-add_integer.py](./0-add_integer.py): Python function that returns the integer addition
  of two numbers.
  * If either of `a` or `b` is not an `int` or `float`, a `TypeError` is raised
  with the message `a must be an integer` or `b must be an integer`.
  * If either of `a` or `b` is a `float`, it is casted to an `int`
  before addition.

* **1. Divide a matrix**
  * [2-matrix_divided.py](./2-matrix_divided.py): Python function that divides all
  elements of a matrix by a common divisor.
  * Returns a new matrix representing the division of all elements of `matrix`
  by `div`.
  * Quotients are rounded to two decimal places.
  * If `matrix` is not a list of lists of `int`s or `float`s, a `TypeError`
  is raised with the message `matrix must be a matrix (list of lists) of
  integers/floats`.
  * If `matrix` contains rows of different lengths, a `TypeError` is raised
  with the message `Each row of the matrix must have the same size`.
  * If the divisor `div` is not an `int` or `float`, a `TypeError` is raised
  with the message `div must be a number`.
  * If `div` is `0`, a `ZeroDivisionError` is raised with the message
  `division by zero`.

* **2. Say my name**
  * [3-say_my_name.py](./3-say_my_name.py): Python function that prints a name in
  the format `My name is <first_name> <last_name>`.
  * If either of `first_name` or `last_name` is not a `str`, a `TypeError` is
  raised with the message `first_name must be a string` or `last_name must be a
  string`.

* **3. Print square**
  * [4-print_square.py](./4-print_square.py): Python function that prints a square using
  the `#` character.
  * The paramter `size` represents the height/width of the square.
  * If `size` is not an `int`, a `TypeError` is raised  with the message,
  `size must be an integer`.
  * If `size` is less than `0`, a `ValueError` is raised with the message `size
  must be >= 0`.

* **4. Text indentation**
  * [5-text_indentation.py](./5-text_indentation.py): Python function that prints text with
  indentation.
  * Two new lines are printed after any `.`, `?`, or `:` character.
  * If `text` is not a `str`, a `TypeError` is raised with the message `text
  must be a string`.
  * No spaces are printed at the beginning or end of each printed line.

* **5. Max integer - Unittest**
  * [tests/6-max_integer_test.py](./tests/6-max_integer_text.py): Python class/script
  that runs unittests for the function `def max_integer(list=[]):`

