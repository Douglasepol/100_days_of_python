'''
Problem: Calculate Circle's Area and Circumference

Given the radius of a circle, write a Python program to calculate the area and the circumference. 
Use the value of pi as 3.14159.

'''

def circle_properties(radius):
    pi = 3.14159
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return (area, circumference)

# Test examples
test_radii = [1, 5, 10]

circle_results = {}

# Iterate through each radius and calculate its circle properties
for radius in test_radii:
    circle_results[radius] = circle_properties(radius)

print(circle_results)