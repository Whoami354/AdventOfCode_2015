lines = open("input", "r", encoding='utf-8').read().strip()
x,y = 0, 0
rx,ry = 0, 0
counter = 0
visited_houses = [(x,y)]

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
        visited_houses.append((x, y))
    else:
        if i == '^':
            ry += 1
        elif i == 'v':
            ry -= 1
        elif i == '>':
            rx += 1
        elif i == '<':
            rx -= 1
        visited_houses.append((rx, ry))
    counter += 1

print("Part 2:",len(set(visited_houses)))