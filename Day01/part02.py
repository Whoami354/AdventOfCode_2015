lines = input = open("input", "r", encoding='utf-8').read().strip()

floor = 0
basement = 0

for i in lines:
    if floor == -1:
        break
    elif i == '(':
        floor += 1
    elif i == ')':
        floor -= 1
    basement += 1

print(basement)
