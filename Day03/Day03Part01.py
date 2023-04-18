lines = open("input", "r", encoding='utf-8').read().strip()
x,y = 0, 0

visited_houses = [(x,y)]
visited_houses = set(visited_houses)

for i in lines:
    if i == '^':
        y += 1
    elif i == 'v':
        y -= 1
    elif i == '>':
        x += 1
    elif i == '<':
        x -= 1
    visited_houses.add((x, y))

print("Part 1:",len(visited_houses))