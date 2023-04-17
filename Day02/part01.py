lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

sum_square = 0
for gift in lines:
    value = gift.split('x')
    length, width, height = int(value[0]), int(value[1]), int(value[2])
    length_width = length * width
    width_height = width * height
    height_length = length * height
    sum_square += (2 * length_width) + (2 * width_height) + (2 * height_length) + min(length_width, width_height,height_length)

print(sum_square)