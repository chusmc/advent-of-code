with open('input.txt', 'r') as input:

    sums=[]
    buffer = [int(input.readline()), int(input.readline()), int(input.readline())]
    sums.append(sum(buffer))

    for line in input.readlines():
        buffer[0] = buffer[1]
        buffer[1] = buffer[2]
        buffer[2] = int(line)
        sums.append(sum(buffer))

previous_depth = sums[0]
counter = 0
for index in range(1, len(sums)):
    current_depth = sums[index]
    if current_depth > previous_depth:
        counter = counter + 1
    previous_depth = current_depth

print('solution', counter)
