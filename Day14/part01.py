lines = input = open("input", "r", encoding='utf-8').read().strip().split('\n')
reindeer = {}
distances = []

for line in lines:
    name, _, _, speed, _, _, duration, _, _, _, _, _, _, rest, _ = line.split()
    reindeer[name] = {'speed': int(speed), 'flight_time': int(duration), 'rest_time': int(rest)}



for r in reindeer:
    cycle_time = reindeer[r]['flight_time'] + reindeer[r]['rest_time']
    cycles, remain = divmod(2503, cycle_time)
    dist = cycles * reindeer[r]['speed'] * reindeer[r]['flight_time']
    if remain > reindeer[r]['flight_time']:
        dist += reindeer[r]['flight_time'] * reindeer[r]['speed']
    else:
        dist += remain * reindeer[r]['speed']
    distances.append(dist)

print(max(distances))