input = open('input.txt', 'r')


horizontal_position = 0
depth = 0

for line in input:
    command, value = line.split(' ')
    value = int(value)
    if command == 'forward':
        horizontal_position = horizontal_position + value
    elif command == 'down':
        depth = depth + value
    elif command == 'up':
        depth = depth - value

print('solutuion ', depth,horizontal_position, horizontal_position * depth)



