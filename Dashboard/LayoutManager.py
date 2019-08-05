import math

Apps_per_Row = 2

def LayerCalculation(num):
    layers = num/Apps_per_Row
    #Check if there are apps left behind...
    if num % 2 != 0:
        layers += 1
    return int(layers)


