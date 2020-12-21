def parse_input():
    day04_input = open('./2020/day_04/input.txt', 'r')
    lines = day04_input.readlines()
    passports = {}
    curr_human = 0

    for line in lines:
        l = line.rstrip('\n')
        if not l:
            curr_human += 1
            continue

        fields = l.split(' ')
        if curr_human not in passports:
            passports[curr_human] = {}

        for field in fields:
            item = field.split(':')
            passports[curr_human][item[0]] = item[1]

    day04_input.close()

    return passports


def count_valid(passports):
    total_valid = 0
    fields_needed = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for human in passports:
        p = passports[human]
        valid = True
        for f in fields_needed:
            if f not in p:
                valid = False
                continue
        total_valid += 1 if valid else 0

    return total_valid


if __name__ == "__main__":
    passports = parse_input()
    part_one_solution = count_valid(passports)

    print(f'The solution to part one is {part_one_solution}')
