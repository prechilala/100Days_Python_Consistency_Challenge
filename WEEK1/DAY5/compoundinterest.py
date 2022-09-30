#!/usr/bin/python3

savings = float(input('Enter the amount deposited:'))
interest1 = savings * 0.04 * 1
interest2 = interest1 * 2
interest3 = interest1 * 3

print(f'The amount in your savings account in the 1st year is\
 {interest1 + savings:.2f}')
print(f'The amount in your savings account in the 2nd year is\
 {interest2 + savings:.2f}')
print(f'The amount in your savings account in the 3rd year is\
 {interest3 + savings:.2f}')
