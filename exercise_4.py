#!/usr/bin/python3
"""
    calculet the area of a field
    Area (feet) = length(feet) * breath(feet)
"""
length = float(input('Input length (feet): '))
breath = float(input('Input breath (feet): '))
Area = (length * breath) /  43560
print("Area = {} sq/ft".format(Area))
