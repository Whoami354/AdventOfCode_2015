lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

sum_ribbon = 0
for i in lines:
    value = i.split('x')
    length, width, height = int(value[0]), int(value[1]), int(value[2])
    lw = 2 * length + 2 * width
    lh = 2 * length + 2 * height
    wh = 2 * width + 2 * height
    ribbon_bow = length * width * height
    sum_ribbon += min(lw, lh, wh) + ribbon_bow

print(sum_ribbon)