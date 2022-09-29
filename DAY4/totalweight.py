#!/usr/bin/python3

widget_weight_in_grams = 75
gizmo_weight_in_grams = 112

widget = int(input('Enter the number of widgets bought:'))
gizmo = int(input('Enter the number of gizmos bought:'))
Total =  widget * widget_weight_in_grams + gizmo * gizmo_weight_in_grams

print('The Total weight of your order is :', Total)
