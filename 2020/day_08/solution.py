

def accumulator_val(instructions):
    acc = 0
    curr = 0

    while instructions:
        i = instructions[curr]
        if i['seen']:
            return acc
        else:
            i['seen'] = True

        if i['opp'] == 'acc':
            acc += i['arg']
        elif i['opp'] == 'jmp':
            curr += i['arg']
            continue

        curr += 1


def read_in_instructions():
    day08_input = open('./2020/day_08/input.txt', 'r')
    lines = day08_input.readlines()
    instructions = {}
    curr = 0

    for line in lines:
        instruction = line.rstrip('\n')
        instruction_split = instruction.split(' ')
        instructions[curr] = {'opp': instruction_split[0], 'arg': int(instruction_split[1]), 'seen': False}
        curr += 1

    day08_input.close()
    return instructions


if __name__ == "__main__":
    instructions = read_in_instructions()
    part_one_solution = accumulator_val(instructions)

    print(f'The solution to part one is {part_one_solution}')
