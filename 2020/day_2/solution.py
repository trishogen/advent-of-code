def num_valid_passwords():
    valid_passwords = 0

    f = open('./2020/day_2/input.txt')
    for line in f:
        line_split = line.rstrip('\n').split(':')
        conditions = line_split[0].split(' ')
        min_max = conditions[0].split('-')

        min_count, max_count = int(min_max[0]), int(min_max[1])
        letter = conditions[1]
        password = line_split[1]

        letter_count = 0
        for char in password:
            if char == letter:
                letter_count += 1

        if max_count + 1 > letter_count > min_count - 1:
            valid_passwords += 1

    f.close()
    return valid_passwords


def num_valid_passwords_new_policy():
    valid_passwords = 0

    f = open('./2020/day_2/input.txt')
    for line in f:
        line_split = line.rstrip('\n').split(':')
        conditions = line_split[0].split(' ')
        letter_placements = conditions[0].split('-')

        first_spot, second_spot = int(letter_placements[0]), int(letter_placements[1])
        letter = conditions[1]
        password = line_split[1].lstrip()

        first_condition = True if password[first_spot - 1] == letter else False
        second_condition = True if password[second_spot - 1] == letter else False

        if first_condition and not second_condition:
            valid_passwords += 1
        elif second_condition and not first_condition:
            valid_passwords += 1

    f.close()
    return valid_passwords


part_one_solution = num_valid_passwords()
part_two_solution = num_valid_passwords_new_policy()

print(f'The solution to part one is {part_one_solution}')
print(f'The solution to part two is {part_two_solution}')
