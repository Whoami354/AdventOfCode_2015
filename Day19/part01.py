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

unique_molecules = set()
for key in replacements:
    for i in range(len(medicine)):
        if medicine[i:i+len(key)] == key:
            for replacement in replacements[key]:
                new_molecule = medicine[:i] + replacement + medicine[i+len(key):]
                unique_molecules.add(new_molecule)

print(len(unique_molecules))