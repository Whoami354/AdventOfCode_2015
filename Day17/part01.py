# Liste der Behältergrößen
lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
newLines = [int(i) for i in lines]

def count_combinations(eggnog, containers):
    # Wenn keine Eggnog mehr übrig ist, haben wir eine gültige Kombination gefunden
    if eggnog == 0:
        return 1
    # Wenn wir mehr Eggnog haben als die größte verfügbare Größe, gibt es keine gültige Kombination
    if eggnog < 0 or not containers:
        return 0
    return count_combinations(eggnog - containers[0], containers[1:]) + count_combinations(eggnog, containers[1:])

print(count_combinations(150, newLines))

