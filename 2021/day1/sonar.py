with open('input.txt', 'r') as input:
    previous_depth = int(input.readline())
    counter = 0
    for line in input.readlines():
        value = int(line)
        current_depth = value
        if current_depth > previous_depth:
            counter = counter + 1
        previous_depth = current_depth

print('solution', counter)
