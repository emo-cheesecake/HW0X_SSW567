# Tamara Gonzalez Ibarra
# SSW 567 - Fall 2025

import unittest
import math
import triangleClassifier

class TestClassifyTriangle(unittest.TestCase):
    
    def test_equilateral_triangle(self):
        self.assertEqual(triangleClassifier.classify_triangle(5, 5, 5), "Equilateral Triangle")
    
    def test_isosceles_triangle(self):
        self.assertEqual(triangleClassifier.classify_triangle(5, 5, 8), "Isosceles Triangle")
    
    def test_scalene_triangle(self):
        self.assertEqual(triangleClassifier.classify_triangle(4, 5, 6), "Scalene Triangle")
    
    def test_right_triangle(self):
        self.assertEqual(triangleClassifier.classify_triangle(3, 4, 5), "Scalene Right Triangle")
    
    def test_invalid_triangles(self):
        self.assertEqual(triangleClassifier.classify_triangle(0, 4, 5), "Invalid Triangle") # input less than 1
        self.assertEqual(triangleClassifier.classify_triangle(1, 2, 3), "Invalid Triangle") # invalid triangle with inputs
    
    def test_non_right_triangle(self):
        self.assertEqual(triangleClassifier.classify_triangle(5, 6, 7), "Scalene Triangle")
    
    def test_isosceles_right_triangle(self):
        self.assertEqual(triangleClassifier.classify_triangle(5, 5, 7.07106781187), "Isosceles Right Triangle")  # close to sqrt(50)
        self.assertEqual(triangleClassifier.classify_triangle(5, 5, math.sqrt(50)), "Isosceles Right Triangle")    
if __name__ == "__main__":
    unittest.main()
