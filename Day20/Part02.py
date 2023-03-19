import numpy as np

goal = 33100000
BIG_NUM = 1000000

house_b = np.zeros(BIG_NUM)

for elf in range(1, BIG_NUM):
    house_b[elf:(elf + 1) * 50: elf] += 11 * elf

print(np.nonzero(house_b >= goal)[0][0])
