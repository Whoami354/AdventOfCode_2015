from itertools import permutations

lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
happiness = {}
max_values = []


for line in lines:
    people = line.split(" ")
    firstperson = people[0]
    secondperson = people[-1][:-1]
    number = int(people[3])
    if "gain" in people:
        happiness[(firstperson, secondperson)] = number
    else:
        assert "lose" in people
        happiness[(firstperson, secondperson)] = -number

# create a list of all the people
# create a list of all the people
people = ["Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory"]

# create a function to calculate the total happiness for a given seating arrangement
def calculate_happiness(seating_arrangement):
    total_happiness = 0
    for i in range(len(seating_arrangement)):
        person1 = seating_arrangement[i]
        person2 = seating_arrangement[(i + 1) % len(seating_arrangement)]
        total_happiness += happiness[person1, person2] + happiness[person2, person1]
    return total_happiness

# calculate the optimal seating arrangement by trying all permutations of the people
optimal_happiness = float('-inf')
for arrangement in permutations(people):
    max_values.append(calculate_happiness(arrangement))

print("The total change in happiness for the optimal seating arrangement is:", max(max_values))