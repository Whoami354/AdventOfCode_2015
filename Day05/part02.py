import re

lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
counter = 0

for i in lines:
    isNice = False
    isTwoLetters = False
    if any([i[j] == i[j + 2] for j in range(len(i) - 2)]):
        isTwoLetters = True
    if any([(i.count(i[k:k + 2]) >= 2) for k in range(len(i) - 2)]):
        isNice = True
    if isNice and isTwoLetters:
        counter += 1

print(counter)
