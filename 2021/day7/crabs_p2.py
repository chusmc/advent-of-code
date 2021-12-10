import math

positions = [int(pos) for pos in open('input.txt', 'r').read().split(',')]
positions.sort()

min_fuel = math.inf
best_pos = -1


def sigma(distance):
    return int((distance * (distance + 1)) / 2)
    
for target in range(positions[0],positions[len(positions) - 1]):
    fuel = 0
    for pos in positions:
        fuel += sigma(abs(pos - target))
        if (fuel > min_fuel):
            break
    if fuel < min_fuel:
        min_fuel = fuel
        best_pos = target


print ('solution', best_pos, min_fuel)

