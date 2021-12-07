

horizontal_position = 0
depth = 0
aim = 0

with open('input.txt', 'r') as input:
    for line in input:
        command, value = line.split()
        value = int(value)
        if command == 'forward':
            horizontal_position = horizontal_position + value
            depth = depth + value * aim
        elif command == 'down':
            aim = aim + value
        elif command == 'up':
            aim = aim - value

print('solutuion ', depth, horizontal_position, horizontal_position * depth)



