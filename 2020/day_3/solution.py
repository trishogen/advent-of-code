def trees_encountered():
    trees = 0
    idx = 0

    f = open('./2020/day_3/input.txt')
    for line in f:
        l = line.rstrip('\n')

        if l[idx] == '#':
            trees += 1

        idx = (idx + 3) % len(l)

    f.close()
    return trees


def trees_encountered_different_routes():
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    result = 1
    forest = make_forest()

    for slope in slopes:
        result = result * toboggan_and_count(forest, slope)

    return result


def toboggan_and_count(forest, slope):
    right, down = slope[0], slope[1]
    curr_down, curr_right = 0, 0
    trees = 0

    while curr_down < len(forest):
        pattern = forest[curr_down]

        if pattern[curr_right] == '#':
            trees += 1

        curr_right = (curr_right + right) % len(pattern)
        curr_down += down

    return trees


def make_forest():
    forest = []
    f = open('./2020/day_3/input.txt')
    for line in f:
        l = line.rstrip('\n')

        forest.append(l)
    f.close()

    return forest


part_one_solution = trees_encountered()
part_two_solution = trees_encountered_different_routes()

print(f'The solution to part one is {part_one_solution}')
print(f'The solution to part two is {part_two_solution}')
