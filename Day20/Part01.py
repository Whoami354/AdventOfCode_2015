import numpy as np

goal = 33100000
BIG_NUM = 1000000

house_a = np.zeros(BIG_NUM)

for elf in range(1, BIG_NUM):
    house_a[elf::elf] += 10 * elf

print(np.nonzero(house_a >= goal)[0][0])