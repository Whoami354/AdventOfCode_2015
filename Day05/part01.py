import re

lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
badString = ['ab', 'cd', 'pq', 'xy']
counter = 0

for line in lines:
    isNice = False
    isTwoLetters = False
    regexp = re.compile(r"(.)\1")
    if regexp.search(line):
        isTwoLetters = True
    vowels = (line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u'))
    if vowels >= 3:
        isNice = True
    for j in badString:
        if j in line:
            isNice = False
    if isNice and isTwoLetters:
        counter += 1


print(counter)