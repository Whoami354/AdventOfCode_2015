lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

replacements = {}
medicine = lines[-1].strip()

for line in lines:
    if "=>" in line:
        line = line.split(" => ")
        key = line[0]
        value = line[1]
        if key in replacements:
            replacements[key].append(value)
        else:
            replacements[key] = [value]

unique_molecules = set()
for key in replacements:
    for i in range(len(medicine)):
        if medicine[i:i+len(key)] == key:
            for replacement in replacements[key]:
                new_molecule = medicine[:i] + replacement + medicine[i+len(key):]
                unique_molecules.add(new_molecule)

print(len(unique_molecules))