#!/usr/bin/python3

small_deposit = 0.10
big_deposit = 0.25

SMALL = int(input('how many containers of 1 litre or less do you have?'))
BIG = int(input('how many containers of more than 1 litre do you have?'))

refund = SMALL * small_deposit + BIG * big_deposit

print('You will be refunded $%.2f, for your containers.'  % refund )
