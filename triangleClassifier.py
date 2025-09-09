# Tamara Gonzalez Ibarra
# SSW 567 - Fall 2025

import math

"""
This function returns a string that classifies whether a triangle is scalene, isosceles, equilateral or a right triangle.
"""
def classify_triangle(length1, length2, length3):

    # Checks for the validity of the triangle and inputs, as they must be greater than 0 and create a valid triangle.
    if length1 <= 0 or length2 <= 0 or length3 <= 0:
        return "Invalid Triangle"
    if not (length1 + length2 > length3 and length1 + length3 > length2 and length2 + length3 > length1):
        return "Invalid Triangle"
    
    # Sorts the sides to identify the largest side (potential hypotenuse)
    sides = sorted([length1, length2, length3])
    a, b, c = sides[0], sides[1], sides[2]
    
    # Uses Pythagorean theorem to determine if the triangle is a right triangle, variable rightTriangleCheck is a boolean.
    rightTriangleCheck = math.isclose(a**2 + b**2, c**2)

    # Classifies the triangle based on sides
    if length1 == length2 == length3:
        triangleType = "Equilateral"
    elif length1 == length2 or length2 == length3 or length1 == length3:
        triangleType = "Isosceles"
    else:
        triangleType = "Scalene"

    # returns type of triangle
    if rightTriangleCheck is True:
        return f"{triangleType} Right Triangle"
    else:
        return f"{triangleType} Triangle"

