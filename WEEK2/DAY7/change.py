#!/usr/bin/python3

#collection of coins needed to represent a number of cents
cents_to_toonie = ct = 200
cents_to_loonie = cl = 100
cents_to_quarter = cq = 25
cents_to_dime = cd = 10
cents_to_nickel = cn = 5

#Number of cents by User
cents = c = int(input("Enter the number of cents: "))

print("Your balance is:")
print(f"{c // ct} toonies,")
c = c % ct
print(f"{c // cl} loonies,")
c = c % cl
print(f"{c // cq} quarters,")
c = c % cq
print(f"{c // cd} dimes,")
c = c % cd
print(f"{c // cn} nickels,")
c = c % cn
print(f"{c} pennies.")
