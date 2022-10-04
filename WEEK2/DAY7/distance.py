#!/usr/bin/python3
import math

x1 = math.radians(float(input("Enter the value of longitude at point 1: ")))
y1 = math.radians(float(input("Enter the value of latitude at point 1: ")))

x2 = math.radians(float(input("Enter the value of longitude at point 2: ")))
y2 = math.radians(float(input("Enter the value of latitude at point 2: ")))

distance = 6371.01 * math.acos(math.sin(x1) * math.sin(y2) + math.cos(x1) * math.cos(y2) * math.cos(y1 - y2))

print(f"\nThe distance between the points = {distance:.2f}km")
