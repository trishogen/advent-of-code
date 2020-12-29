
def find_first_invalid():
    day09_input = open('./2020/day_09/input.txt', 'r')
    lines = day09_input.readlines()
    numbers = []
    invalid = None

    for line in lines:
        num = int(line.rstrip('\n'))
        numbers.append(num)
        if len(numbers) > 26:
            numbers.pop(0)
            ans = is_valid(numbers, num)
            if not ans:
                invalid = num
                break

    day09_input.close()
    return invalid


def is_valid(arr, total):
    seen = {}

    for i in arr:
        sub_total = total - i
        if sub_total not in seen:
            seen[i] = True
        else:
            return True

    return False


if __name__ == "__main__":
    part_one_solution = find_first_invalid()

    print(f'The solution to part one is {part_one_solution}')
