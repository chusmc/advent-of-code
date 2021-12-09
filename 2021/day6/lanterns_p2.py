lantern_days = {}
for d in open('input.txt', 'r').read().split(','):
    lantern_days[int(d)] = lantern_days.get(int(d), 0) + 1

print(lantern_days.get(0,0), lantern_days.get(1,0), lantern_days.get(2,0), lantern_days.get(3,0), lantern_days.get(4,0), lantern_days.get(5,0), lantern_days.get(6,0), lantern_days.get(7,0), lantern_days.get(8,0))


max_days = 256
give_birth = 0

for i in range(max_days):
    give_birth = lantern_days.get(0, 0)

    for d in range(0, 8):
        lantern_days[d] = lantern_days.get(d + 1, 0)

    lantern_days[6] = lantern_days.get(6, 0) + give_birth
    lantern_days[8] = give_birth

    print(lantern_days.get(0,0), lantern_days.get(1,0), lantern_days.get(2,0), lantern_days.get(3,0), lantern_days.get(4,0), lantern_days.get(5,0), lantern_days.get(6,0), lantern_days.get(7,0), lantern_days.get(8,0))


total = 0
for d in range(0, 9):
    total = total + lantern_days.get(d, 0)

print ('solution', total)

