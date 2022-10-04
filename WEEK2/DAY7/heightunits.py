#!/usr/bin/python3

inch_per_feet = 12
cm_per_inch = 2.54

print("Enter your height:")

feet = int(input("Height in feet: "))
inches = int(input("Height in inches: "))
height_in_cm = ((feet * inch_per_feet) + inches) * cm_per_inch

print(f"\nYour height in cm is {height_in_cm}")
