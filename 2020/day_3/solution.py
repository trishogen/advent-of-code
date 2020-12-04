def trees_encountered():
    trees = 0
    idx = 0

    f = open('./2020/day_3/input.txt')
    for line in f:
        l = line.rstrip('\n')
        pattern = [char for char in l]

        if pattern[idx] == '#':
            trees += 1

        tmp_idx = idx + 3
        pattern_size = len(pattern)
        idx = tmp_idx % pattern_size if tmp_idx > pattern_size - 1 else tmp_idx

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

    trees = []
    forest = make_forest()

    for slope in slopes:
        trees.append(toboggan_and_count(forest, slope))

    result = 1
    for tree in trees:
        result = result * tree

    return result


def toboggan_and_count(forest, slope):
    right, down = slope[0], slope[1]
    curr_down, curr_right = 0, 0
    trees = 0

    while curr_down < len(forest):
        pattern = forest[curr_down]
        position = pattern[curr_right]
        if position == '#':
            trees += 1

        tmp_idx = curr_right + right
        pattern_size = len(pattern)
        curr_right = tmp_idx % pattern_size if tmp_idx > pattern_size - 1 else tmp_idx
        curr_down += down

    return trees


def make_forest():
    forest = []
    f = open('./2020/day_3/input.txt')
    for line in f:
        l = line.rstrip('\n')
        pattern = [char for char in l]

        forest.append(pattern)
    f.close()

    return forest


part_one_solution = trees_encountered()
part_two_solution = trees_encountered_different_routes()

print(f'The solution to part one is {part_one_solution}')
print(f'The solution to part two is {part_two_solution}')
