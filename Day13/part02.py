import itertools
from itertools import permutations

lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
happiness = {}
max_values = []
people = set()

for line in lines:
    allpeople = line.split(" ")
    firstperson = allpeople[0]
    secondperson = allpeople[-1][:-1]
    number = int(allpeople[3])

    people.add(firstperson)
    people.add(secondperson)

    if "gain" in allpeople:
        happiness[firstperson + secondperson] = number
    else:
        assert "lose" in allpeople
        happiness[firstperson + secondperson] = -number

# create a function to calculate the total happiness for a given seating arrangement
def calculate_happiness(people, happiness):
    maximum_happiness = 0
    for arragement in itertools.permutations(people):
        happiness_gained = 0
        for person1, person2 in zip(arragement[:-1], arragement[1:]):
            happiness_gained += happiness[person1 + person2]
            happiness_gained += happiness[person2 + person1]
        # add happiness for first and last pair
        person1 = arragement[0]
        person2 = arragement[-1]
        #print("person 1 and person 2", happiness[person1 + person2], person1, person2)
        happiness_gained += happiness[person1 + person2]
        #print("person 2 and person 1", happiness[person1 + person2], person1, person2)
        happiness_gained += happiness[person2 + person1]
        maximum_happiness = max(maximum_happiness, happiness_gained)

    return maximum_happiness


# calculate the optimal seating arrangement by trying all permutations of the people
optimal_happiness = float('-inf')
for person in people:
    happiness['Self' + person] = 0
    happiness[person + 'Self'] = 0
people.add('Self')
print(calculate_happiness(people, happiness))
