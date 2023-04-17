lines = open("input", "r", encoding='utf-8').read().strip()
x,y = 0, 0

visited_houses = [(x,y)]

for i in lines:
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
print("Part 1:",len(set(visited_houses)))