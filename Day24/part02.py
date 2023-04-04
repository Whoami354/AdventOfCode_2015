import itertools

def find_smallest_group(packages):
    target_weight = sum(packages) // 4
    smallest_qe = float('inf')

    for i in range(0, len(packages)):
        combinations = itertools.combinations(packages, i)
        valid_combinations = [c for c in combinations if sum(c) == target_weight]

        for valid in valid_combinations:
            qe = 1
            for p in valid:
                qe *= p

            smallest_qe = min(smallest_qe, qe)
            print(smallest_qe)

    return smallest_qe

packages = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
smallest_qe = find_smallest_group(packages)
print(smallest_qe)
