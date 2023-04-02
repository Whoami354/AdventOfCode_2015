lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

a = 1
b = 0

def hlf(r):
    global a, b
    if r == 'a':
        a //= 2
    elif r == 'b':
        b //= 2

def tpl(r):
    global a, b
    if r == 'a':
        a *= 3
    elif r == 'b':
        b *= 3

def inc(r):
    global a, b
    if r == 'a':
        a += 1
    elif r == 'b':
        b += 1

def jmp(offset):
    global a, b
    return offset

def jie(r, offset):
    global a, b
    if r == 'a':
        if a % 2 == 0:
            return offset
        else:
            return 1
    elif r == 'b':
        if b % 2 == 0:
            return offset
        else:
            return 1

def jio(r, offset):
    global a, b
    if r == 'a':
        if a == 1:
            return offset
        else:
            return 1
    elif r == 'b':
        if b == 1:
            return offset
        else:
            return 1

i = 0
while i < len(lines):
    instr = lines[i].split()
    if instr[0] == 'hlf':
        hlf(instr[1])
        i += 1
    elif instr[0] == 'tpl':
        tpl(instr[1])
        i += 1
    elif instr[0] == 'inc':
        inc(instr[1])
        i += 1
    elif instr[0] == 'jmp':
        i += jmp(int(instr[1]))
    elif instr[0] == 'jie':
        i += jie(instr[1][0], int(instr[2]))
    elif instr[0] == 'jio':
        i += jio(instr[1][0], int(instr[2]))

print(b)