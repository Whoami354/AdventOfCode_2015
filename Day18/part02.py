lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

lights = [[False for _ in range(100)] for _ in range(100)]
for i, row in enumerate(lines):
    for j, char in enumerate(row):
        if char == '#':
            lights[i][j] = True

lights[0][0] = lights[0][99] = lights[99][0] = lights[99][99] = True


def next_light_state(lights_two):
    new_lights = [[False for _ in range(100)] for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if (i == 0 and j == 0) or (i == 0 and j == 99) or (i == 99 and j == 0) or (i == 99 and j == 99):
                new_lights[i][j] = True
                continue
            neighbors_on = 0
            for x_offset in [-1, 0, 1]:
                for y_offset in [-1, 0, 1]:
                    if x_offset == 0 and y_offset == 0:
                        continue
                    x = i + x_offset
                    y = j + y_offset
                    if 0 <= x < 100 and 0 <= y < 100 and lights_two[x][y]:
                        neighbors_on += 1
            if lights_two[i][j] and (neighbors_on == 2 or neighbors_on == 3):
                new_lights[i][j] = True
            elif not lights_two[i][j] and neighbors_on == 3:
                new_lights[i][j] = True
    return new_lights


for _ in range(100):
    lights = next_light_state(lights)

print(sum([sum(row) for row in lights]))
