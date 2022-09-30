#!/usr/bin/python3

from math import log10

a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))

print(a, '+', b, 'is', a + b)
print(a, '-', b, 'is', a - b)
print(a, '*', b, 'is', a * b)
print(a, '/', b, 'is', a / b)
print(a, '%', b, 'is', a % b)
print('The base 10 log of', a, 'is', log10(a))
print(a, '^', b, 'is', a ** b)
