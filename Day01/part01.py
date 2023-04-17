lines = open("input", "r", encoding='utf-8').read().strip()

floor = 0
for i in lines:
    if i == '(':
        floor += 1
    elif i == ')':
        floor -= 1

print(lines.count('(') - lines.count(')'))