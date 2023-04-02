from itertools import combinations
from math import prod

packages = [
    1, 3, 5, 11, 13, 17, 19, 23, 29, 31,
    41, 43, 47, 53, 59, 61, 67, 71, 73,
    79, 83, 89, 97, 101, 103, 107, 109, 113
]


def split_packages(packages, num_groups):
    target_weight, remainder = divmod(sum(packages), num_groups)
    if remainder != 0:
        return None

    for group_size in range(1, len(packages)):
        for first_group in combinations(packages, group_size):
            if sum(first_group) != target_weight:
                continue

            remaining_packages = set(packages) - set(first_group)
            for second_group in combinations(remaining_packages, len(remaining_packages) // 2):
                third_group = remaining_packages - set(second_group)
                if sum(second_group) == sum(third_group):
                    return first_group, second_group, third_group


groups = split_packages(packages, 3)
qe_values = [prod(g) for g in groups]
min_qe = min(qe_values)

for g, qe in zip(groups, qe_values):
    if prod(g) == min_qe:
        print(min_qe)
        break
