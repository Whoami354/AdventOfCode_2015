import numpy as np

lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
grid = np.zeros((1000, 1000), dtype = int)

for line in lines:
    lline = line.split(" ")
    if lline[0] == 'turn':
        x1, y1 = lline[2].split(',')
        x2, y2 = lline[4].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if lline[1] == 'on':
            grid[x1:x2 + 1, y1:y2 + 1] += 1
        else:
            assert lline[1] == 'off'
            grid[x1:x2 + 1, y1:y2 + 1] += -1
            grid[grid < 0] = 0
    else:
        assert lline[0] == 'toggle'
        x1, y1 = lline[1].split(',')
        x2, y2 = lline[3].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2 + 1, y1:y2 + 1] += 2

print(np.sum(grid))
