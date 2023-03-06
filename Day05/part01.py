import re

lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
badString = ['ab', 'cd', 'pq', 'xy']
counter = 0

for i in lines:
    isNice = False
    isTwoLetters = False
    regexp = re.compile(r"(.)\1")
    if regexp.search(i):
        isTwoLetters = True
    vowels = (i.count('a') + i.count('e') + i.count('i') + i.count('o') + i.count('u'))
    if vowels >= 3:
        isNice = True
    for j in badString:
        if j in i:
            isNice = False
    if isNice and isTwoLetters:
        counter += 1


print(counter)