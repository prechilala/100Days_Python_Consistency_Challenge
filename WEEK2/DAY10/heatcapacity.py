#!/usr/bin/python3

water_heat_capacity = whc = 4.186
joules_to_kilowatt_hours = X = 0.0000002778
price_of_electrcity = pof = 8.9

volume = v = float(input('Enter the amount of water in milliliters:'))
temp = t = float(input('Enter the temperature increase in degrees celsius:'))

energy_in_joules = Y = v * t * whc

print('This will require %d joules of energy.' % Y)

kilowatt_hours = kwh = Y * X
cost = kwh * pof

print('This much energy will cost you %.2f cents' % cost)
