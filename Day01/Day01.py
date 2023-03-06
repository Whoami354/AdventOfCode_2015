lines = input = open("input", "r", encoding='utf-8').read().strip()

def solution_day(part):
    floor = 0
    basement_position = 0
    for i in lines:
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1
        basement_position += 1
        if floor == -1 and part == 2:
            return basement_position
    if part == 1:
        return floor

print(solution_day(1))
print(solution_day(2))