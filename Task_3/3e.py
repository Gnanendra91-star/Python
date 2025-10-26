# Step 1: Create folder
!mkdir -p my_toolkit
# geometry_utils.py
%%writefile my_toolkit/geometry_utils.py
import math

def area_circle(radius):
    return math.pi * radius ** 2

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)
# text_utils.py
%%writefile my_toolkit/text_utils.py
def to_uppercase(s):
    return s.upper()

def word_count(s):
    return len(s.split())

def is_palindrome(s):
    s_clean = ''.join(s.lower().split())
    return s_clean == s_clean[::-1]
  # __init__.py
%%writefile my_toolkit/__init__.py
from .geometry_utils import area_circle, perimeter_rectangle, pythagoras
from .text_utils import to_uppercase, word_count, is_palindrome
from my_toolkit import area_circle, perimeter_rectangle, pythagoras
from my_toolkit import to_uppercase, word_count, is_palindrome

# Geometry functions
print("Area of circle (r=5):", round(area_circle(5), 2))
print("Perimeter of rectangle (4x6):", perimeter_rectangle(4, 6))
print("Hypotenuse (3,4):", round(pythagoras(3, 4), 2))

# Text functions
print("Uppercase:", to_uppercase("Programming"))
print("Word count:", word_count("Python is fun"))
print("Is palindrome (level):", is_palindrome("radar"))

output:
rea of circle (r=5): 78.54
Perimeter of rectangle (4x6): 20
Hypotenuse (3,4): 5.0
Uppercase: PROGRAMMING
Word count: 3
Is palindrome (radar): True
