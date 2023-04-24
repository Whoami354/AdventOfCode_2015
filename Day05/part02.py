lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
counter = 0

for actualString in lines:
    isNice = False
    isTwoLetters = False
    if any([actualString[j] == actualString[j + 2] for j in range(len(actualString) - 2)]):
        isTwoLetters = True
    if any([(actualString.count(actualString[k:k + 2]) >= 2) for k in range(len(actualString) - 2)]):
        isNice = True
    if isNice and isTwoLetters:
        counter += 1

print(counter)
