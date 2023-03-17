lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

grid = [[1 if c == '#' else 0 for c in row] for row in lines]
height, width = len(grid), len(grid[0])

def next_light_state(row, col):
    on_neighbors = 0
    for i in range(max(row - 1, 0), min(row + 2, height)):
        for j in range(max(col - 1, 0), min(col + 2, width)):
            if i == row and j == col:
                continue
            on_neighbors += grid[i][j]
    if grid[row][col] == 1 and on_neighbors in [2, 3]:
        return 1
    elif grid[row][col] == 0 and on_neighbors == 3:
        return 1
    else:
        return 0

for _ in range(100):
    grid = [[next_light_state(i, j) for j in range(width)] for i in range(height)]

print(sum(sum(row) for row in grid))