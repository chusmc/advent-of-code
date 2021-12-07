
def split_data(data, bit_index):
    bit_one_scans = []
    bit_zero_scans = []
    for scan in data:
        if scan & (1 << bit_index) != 0:
            bit_one_scans.append(scan)
        else:
            bit_zero_scans.append(scan)
    return bit_one_scans, bit_zero_scans

def calculate_gas(data, number_of_bits, selector):
    bit_index = number_of_bits - 1
    while len(data) > 1 and bit_index >= 0:
        bit_one_scans, bit_zero_scans = split_data(data, bit_index)
        if selector(bit_one_scans, bit_zero_scans) == 1:
            data = bit_one_scans
        else:
            data = bit_zero_scans

        bit_index -= 1
    return data[0]

with open('input.txt', 'r') as input:
    data = [int(line,2) for line in input.readlines()]

oxygen = calculate_gas(data, 12, lambda b1,b0: 1 if len(b1) >= len(b0) else 0)
co2 = calculate_gas(data, 12, lambda b1,b0: 0 if len(b0) <= len(b1) else 1)


print(oxygen)
print(co2)
print('solution',  oxygen * co2)






