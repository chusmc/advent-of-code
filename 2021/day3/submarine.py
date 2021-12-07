
number_of_bits = 12
bit_counters = [0] * number_of_bits
total_scans = 0
with open('input.txt', 'r') as input:
    for line in input:
        scan = int(line, 2)
        for bit_index in range(0, number_of_bits):
            bit_is_set = (scan & (1 << bit_index)) != 0
            bit_counters[bit_index] += int(bit_is_set)

        total_scans += 1

gamma = 0
epsilon = 0
for bit_index in range(0, number_of_bits):
    bit_value = int(total_scans - bit_counters[bit_index] < bit_counters[bit_index])
    gamma = gamma | (bit_value << bit_index)
    epsilon = epsilon |  ((not bit_value) << bit_index)
print(gamma)
print(epsilon)
print('solution',  gamma * epsilon)






