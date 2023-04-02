program = [['jio', 'a', '+22'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['tpl', 'a'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['jmp', '+19'],
           ['tpl', 'a'],
           ['tpl', 'a'],
           ['tpl', 'a'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['tpl', 'a'],
           ['tpl', 'a'],
           ['jio', 'a', '+8'],
           ['inc', 'b'],
           ['jie', 'a', '+4'],
           ['tpl', 'a'],
           ['inc', 'a'],
           ['jmp', '+2'],
           ['hlf', 'a'],
           ['jmp', '-7']
           ]

def execute_program(program):
    registers = {'a': 0, 'b': 0}
    pc = 0

    while pc >= 0 and pc < len(program):
        instruction = program[pc]
        opcode = instruction[0]
        arg1 = instruction[1]

        if opcode == 'hlf':
            registers[arg1] //= 2
            pc += 1
        elif opcode == 'tpl':
            registers[arg1] *= 3
            pc += 1
        elif opcode == 'inc':
            registers[arg1] += 1
            pc += 1
        elif opcode == 'jmp':
            pc += int(arg1)
        elif opcode == 'jie':
            if registers[arg1] % 2 == 0:
                pc += int(instruction[2])
            else:
                pc += 1
        elif opcode == 'jio':
            if registers[arg1] == 1:
                pc += int(instruction[2])
            else:
                pc += 1

    return registers['b']

result = execute_program(program)
print(result)
