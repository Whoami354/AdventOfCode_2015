lines = open("input", "r", encoding='utf-8').read().strip()
x,y = 0, 0
rx,ry = 0, 0
counter = 0
visited_houses = [(x,y)]
robo_santa_visited_houses = [(rx,ry)]
atLeastOneVisit = []
result = []

for i in lines:
    if counter % 2 == 0:
        if i == '^':
            y += 1
        elif i == 'v':
            y -= 1
        elif i == '>':
            x += 1
        elif i == '<':
            x -= 1
        coordinates = (x, y)
        visited_houses.append(coordinates)
    else:
        if i == '^':
            ry += 1
        elif i == 'v':
            ry -= 1
        elif i == '>':
            rx += 1
        elif i == '<':
            rx -= 1
        robo_coordinates = (rx, ry)
        robo_santa_visited_houses.append(robo_coordinates)
    counter += 1
result += visited_houses + robo_santa_visited_houses
print("Part 2:",len(set(result)))