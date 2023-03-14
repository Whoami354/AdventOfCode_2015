import json
lines = input = open("input", "r", encoding='utf-8').read().strip()

def sum_numbers(obj):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(sum_numbers(elem) for elem in obj)
    elif isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum(sum_numbers(value) for value in obj.values())
    else:
        return 0


json_obj = json.loads(lines)

total_sum = sum_numbers(json_obj)

print(total_sum)
