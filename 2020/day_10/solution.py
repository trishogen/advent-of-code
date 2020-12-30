
def find_jolt_difference(adapters):
    adapters.sort()
    one_jolt = 0
    three_jolt = 1
    prev = 0

    for i in range(0, len(adapters)):
        diff = adapters[i] - prev

        if diff == 1:
            one_jolt += 1
        elif diff == 3:
            three_jolt += 1

        prev = adapters[i]

    return one_jolt * three_jolt


def get_adapters():
    day10_input = open('./2020/day_10/input.txt', 'r')
    lines = day10_input.readlines()
    adapters = []

    for line in lines:
        num = int(line.rstrip('\n'))
        adapters.append(num)

    day10_input.close()
    return adapters


if __name__ == "__main__":
    adapters = get_adapters()
    part_one_solution = find_jolt_difference(adapters)

    print(f'The solution to part one is {part_one_solution}')
