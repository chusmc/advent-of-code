lanterns = [int(day) for day in open('input.txt', 'r').read().split(',')]

max_days = 80
give_birth = 0
print(lanterns)

for i in range(max_days):
    for d in range(len(lanterns)):

        if lanterns[d] == 0:
            lanterns[d] = 6
            give_birth += 1
        else:
            lanterns[d] -= 1

    lanterns += [8 for nb in range(give_birth)]    
    give_birth = 0


    print(len(lanterns))
print ('solution', len(lanterns))

