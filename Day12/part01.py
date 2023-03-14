import json
lines = input = open("input", "r", encoding='utf-8').read().strip()
def sum_numbers(json_str):
    total_sum = 0
    data = json.loads(json_str)

    if isinstance(data, int):
        return data

    if isinstance(data, list):
        for item in data:
            total_sum += sum_numbers(json.dumps(item))

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, int):
                total_sum += value
            else:
                total_sum += sum_numbers(json.dumps(value))

    return total_sum

print(sum_numbers(lines))