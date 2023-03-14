# https://adventofcode.com/2015/day/8

#"" -> 0
#\\, \", \xXX -> 1

import re

infile = open('input','r')
infileContent = infile.readlines()
infile.close()

summeZeichenVorher = 0
summeZeichenNachher = 0

for line in infileContent:
    print(line[:-1])
    print(len(line))
    summeZeichenVorher += len(line) - 1
    line = line[1:-2] # des letzte in \n deshalb -2!
    line = re.sub('\\\\x[a-f0-9][a-f0-9]', 'X', line)
    line = line.replace('\\"', '\"')
    line = line.replace('\\\\', '\\')
    summeZeichenNachher += len(line)
    print(line)
    print(len(line))

print(summeZeichenVorher)
print(summeZeichenNachher)
print("Ergebnis: %d" % (summeZeichenVorher - summeZeichenNachher)) # 1333
