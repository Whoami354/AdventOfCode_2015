lines = open("input", "r", encoding='utf-8').read().strip().split('\n')


def calculate_ribbon():
    sum_ribbon = 0
    for i in lines:
        value = i.split('x')
        length = int(value[0])
        width = int(value[1])
        height = int(value[2])
        lw = 2 * length + 2 * width
        lh = 2 * length + 2 * height
        wh = 2 * width + 2 * height
        ribbon_bow = length * width * height
        sum_ribbon += min(lw,lh,wh) + ribbon_bow
    return sum_ribbon


def calculate_square():
    sum_square = 0
    sum_ribbon = 0
    for i in lines:
        value = i.split('x')
        length = int(value[0])
        width = int(value[1])
        height = int(value[2])
        length_width = length * width
        width_height = width * height
        height_length = length * height
        sum_square += (2 * length_width) + (2 * width_height) + (2 * height_length) + min(length_width, width_height,
                                                                                          height_length)
    return sum_square


print("Part 1:",calculate_square())
print("Part 2:",calculate_ribbon())