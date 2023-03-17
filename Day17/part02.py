# Liste der Behältergrößen
lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
newLines = [int(i) for i in lines]
eggnog = 150

# Sortiere die Behälter in absteigender Reihenfolge
containers = sorted(newLines, reverse=True)

# Verwende das greedy Algorithmus, um die minimalen Anzahl der Behälter zu finden
total = 0
min_containers = 0
for i in range(len(containers)):
    total += containers[i]
    min_containers += 1
    if total >= eggnog:
        break

# Finde alle Kombinationen von Behältern, die genau 150 Liter ergeben
from itertools import combinations
count = 0
for i in range(1, min_containers + 1):
    for combination in combinations(containers, i):
        if sum(combination) == eggnog:
            count += 1

print("Anzahl der Möglichkeiten, diese zu füllen:", count)