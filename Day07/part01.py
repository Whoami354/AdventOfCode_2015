lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

"""
Interessante Aspekte:
1. Bestimmung ob Wert schon berechnet per Exception
2. Zwei Dictiornaries: 
   - Gatter: {ergebnis: [wert1, OPERATOR, wert2], ...}
   - Ergebnisse: {variablenname : wert} (wird durch die Rekursion gefüllt)
3. Tiefe rekursion 
"""


def calculate(name, tiefe):
    # ist der wert schon berechnet, dann wird er zurückgegeben
    try:
        return int(name)
    except ValueError:
        pass

    print("Tiefe:" + str(tiefe) + " Name: " + name + " Operation: " + str(logikgatter[name]))
    tiefe += 1
    # wenn es zu der Variable noch keinen Wert gibt --> los
    if name not in ergebnisse:
        # hole die Operation - rechne die fehlenden Werte ggf. rekursiv aus
        ops = logikgatter[name]
        if len(ops) == 1:
            res = calculate(ops[0], tiefe)
        else:
            op = ops[-2]
            if op == 'AND':
                res = calculate(ops[0], tiefe) & calculate(ops[2], tiefe)
            elif op == 'OR':
                res = calculate(ops[0], tiefe) | calculate(ops[2], tiefe)
            elif op == 'NOT':
                res = ~calculate(ops[1], tiefe) & 0xffff
            elif op == 'RSHIFT':
                res = calculate(ops[0], tiefe) >> calculate(ops[2], tiefe)
            elif op == 'LSHIFT':
                res = calculate(ops[0], tiefe) << calculate(ops[2], tiefe)
        ergebnisse[name] = res

    return ergebnisse[name]


# log geht's
logikgatter = dict()
ergebnisse = dict()

# dict mit ergebnis: [a, operator, b]
for line in lines:
    (ops, res) = line.split('->')
    logikgatter[res.strip()] = ops.strip().split(' ')

outfile = open('output.txt', 'w')
outfile.write('Eingabewerte:\n')
for key in logikgatter.keys():
    outfile.write(key + " -> " + str(logikgatter[key]) + "\n")

print("a: %d" % calculate('a', 1))

outfile.write('Ausgabewerte:\n')
outfile.write('Gatter mit Werten:\n')
for key in logikgatter.keys():
    outfile.write(key + " -> " + str(logikgatter[key]) + "\n")

outfile.write('Ergebnisse:\n')
for key in ergebnisse.keys():
    outfile.write(key + " -> " + str(ergebnisse[key]) + "\n")
outfile.close()
