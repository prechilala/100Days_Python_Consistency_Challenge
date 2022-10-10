#!/usr/bin/python3

ideal_gas_constant = r = 8.314

pressure = p = float(input("Enter pressure in Pascal: "))
volume = v = float(input("Enter volume in liters: "))
temperature = t = float(input("Enter temperature in degrees Celsius: "))
#temperature in kelvin

t += 273.15
Amount_of_gas_in_moles = n = (p * v) / (r * t)

print(f"The amount of gas is {n:.2f} moles.")
