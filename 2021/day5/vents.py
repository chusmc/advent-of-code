X = 0
Y = 1

def line_points(p1, p2): 
    if p1[X] == p2[X]:
        return [(p1[X], y) for y in range(min(p1[Y], p2[Y]), max(p1[Y], p2[Y]) + 1)]
    elif p1[Y] == p2[Y]:
        return [(x, p2[Y]) for x in range(min(p1[X], p2[X]), max(p1[X], p2[X]) + 1)]
    else:
        return []

def parse_point(pstring):
    x,y = pstring.split(',')
    return (int(x), int(y))

with open('input.txt', 'r') as input:
    vectors = [(parse_point(p1.strip()), parse_point(p2.strip())) for p1,p2 in [line.split('->') for line in input.readlines()]]
        
map_of_points = {}
for vector in vectors:
    points_in_line = line_points(vector[0], vector[1])
    for point in points_in_line:
        map_of_points[point] = map_of_points.get(point, 0) + 1
        
counter = sum(freq >=2 for point,freq in map_of_points.items())
print ('solution', counter)
