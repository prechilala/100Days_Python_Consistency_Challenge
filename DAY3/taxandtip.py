#!/usr/bin/python3

TaxRate = 0.04
TipRate = 0.18

Cost = float(input('Enter the cost of the meal:'))

Tax = Cost * TaxRate
Tip = Cost * TipRate
Total = Cost + Tax + Tip

print('Tax : %.2f' % Tax)
print('Tip : %.2f' % Tip)
print('The total cost your meal : %.2f' % Total) 
