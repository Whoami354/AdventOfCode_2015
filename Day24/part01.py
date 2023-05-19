from itertools import combinations

def quantum_entanglement(packages):
    return 1 if not packages else packages[0] * quantum_entanglement(packages[1:])

def find_groups(packages):
    total_weight = sum(packages)
    group_weight = total_weight // 3

    for group_size in range(1, len(packages)):
        for first_group in combinations(packages, group_size):
            if sum(first_group) == group_weight:
                remaining_packages = [p for p in packages if p not in first_group]
                for second_group_size in range(1, len(remaining_packages)):
                    for second_group in combinations(remaining_packages, second_group_size):
                        if sum(second_group) == group_weight:
                            third_group = [p for p in remaining_packages if p not in second_group]
                            if sum(third_group) == group_weight:
                                return first_group, second_group, third_group

    return None

packages = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

groups = find_groups(packages)
if groups:
    first_group, second_group, third_group = groups
    print("First group:", first_group)
    print("Second group:", second_group)
    print("Third group:", third_group)
    print("Quantum entanglement of first group:", quantum_entanglement(first_group))
else:
    print("No solution found.")
