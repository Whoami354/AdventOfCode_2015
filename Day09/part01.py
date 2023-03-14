lines = input = open("input", "r", encoding='utf-8').read().strip().split("\n")
import itertools

#lines = ['London to Dublin = 464', 'London to Belfast = 518', 'Dublin to Belfast = 141']
distances = {}
values = []

for line in lines:
    values = line.split(" ")
    origin, destination, distance = values[0], values[2], int(values[4])
    distances[(origin, destination)] = distance
    distances[(destination, origin)] = distance

locations = list(set(itertools.chain.from_iterable(distances.keys())))

# initialize shortest distance to infinity
shortest_distance = float("inf")

# find the shortest distance by trying all possible routes
for route in itertools.permutations(locations):
    # calculate the total distance of the route
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances.get((route[i + 1], route[i]), 0)
    # update the shortest distance if this route is shorter
    if total_distance < shortest_distance:
        shortest_distance = total_distance

print(shortest_distance)