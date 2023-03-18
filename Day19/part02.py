lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

replacements = {}
medicine = ""

for line in lines:
    if "=>" in line:
        line = line.split(" => ")
        key = line[0]
        value = line[1]
        if key in replacements:
            replacements[key].append(value)
        else:
            replacements[key] = [value]
    elif not "=>" in line and len(line) > 0:
        medicine += line

