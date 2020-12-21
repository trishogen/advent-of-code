def report_repair_part_one():
    expenses = {}
    cur_expense, paired_expense = None, None

    f = open('./2020/day_01/input.txt')
    for line in f:
        cur_expense = int(line)
        paired_expense = 2020 - cur_expense

        if paired_expense in expenses.keys():
            break

        expenses[cur_expense] = True

    f.close()
    return cur_expense * paired_expense


def report_repair_part_two():
    expenses = []

    f = open('./2020/day_01/input.txt')
    for line in f:
        expenses.append(int(line))

    expenses.sort()
    expenses_size = len(expenses)

    for i in range(0, expenses_size - 2):
        curr_sum = 2020 - expenses[i]
        left = i + 1
        right = expenses_size - 1

        while left < right:
            if curr_sum - expenses[left] - expenses[right] == 0:
                return expenses[i] * expenses[left] * expenses[right]
            elif curr_sum - expenses[left] - expenses[right] < 0:
                right -= 1
            else:
                left += 1


part_one_solution = report_repair_part_one()
part_two_solution = report_repair_part_two()

print(f'The solution to part one is {part_one_solution}')
print(f'The solution to part two is {part_two_solution}')
