import random

# lines = [line for line in open('input')]
#
# medicine = lines[-1].strip()
#
## LHS, RHS sorted with largest LHS first
lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
replacements = [(l.split()[0], l.split()[-1]) for l in lines if '=>' in l]
# replacements.sort(key=lambda x: len(x[0]))
# replacements = replacements[::-1]
#
## greedy replacement on medicine, counting steps
# total = 0
# while medicine != 'e':
#    for lhs, rhs in replacements:
#        if lhs in medicine:
#            medicine = medicine.replace(lhs, rhs, 1)
#            total += 1
#            break
# print(total)

medicine = lines[-1].strip()
newLines = lines[:-2]


def get_total(replacements, medicine):
    original = medicine
    total = 0

    while medicine != 'e':
        current = medicine
        for lhs, rhs in replacements:
            if rhs not in medicine:
                continue

            medicine = medicine.replace(rhs, lhs, 1)
            total += 1

        if current == medicine:
            medicine = original
            total = 0
            random.shuffle(replacements)

    print(total)


get_total(replacements, medicine)
