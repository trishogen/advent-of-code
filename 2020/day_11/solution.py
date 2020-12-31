from copy import deepcopy


def count_occupied_seats(seats):
    occupied = 0
    moved_around = True

    while moved_around:
        moved_around = people_move_around(seats)

    for r in range(0, len(seats)):
        for c in range(0, len(seats[0])):
            if seats[r][c] == '#':
                occupied += 1

    return occupied


def people_move_around(seats):
    copy = deepcopy(seats)

    for r in range(0, len(seats)):
        for c in range(0, len(seats[0])):
            count_adj = num_adjacent_occupied(copy, r, c)
            if copy[r][c] == 'L' and count_adj == 0:
                seats[r][c] = '#'
            elif copy[r][c] == '#' and count_adj >= 4:
                seats[r][c] = 'L'

    return not seats == copy


def num_adjacent_occupied(seats, r, c):
    count = 0
    if r - 1 >= 0 and seats[r - 1][c] == '#':  # above
        count += 1
    if r + 1 < len(seats) and seats[r + 1][c] == '#':  # below
        count += 1
    if c - 1 >= 0 and seats[r][c - 1] == '#':   # left
        count += 1
    if c + 1 < len(seats[0]) and seats[r][c + 1] == '#':   # right
        count += 1
    if c - 1 >= 0 and r - 1 >= 0 and seats[r - 1][c - 1] == '#':   # top left diagonal
        count += 1
    if r - 1 >= 0 and c + 1 < len(seats[0]) and seats[r - 1][c + 1] == '#':   # top right diagonal
        count += 1
    if r + 1 < len(seats) and c - 1 >= 0 and seats[r + 1][c - 1] == '#':  # bottom left diagonal
        count += 1
    if r + 1 < len(seats) and c + 1 < len(seats[0]) and seats[r+1][c+1] == '#':  # bottom right diagonal
        count += 1

    return count


def get_seats():
    day11_input = open('./2020/day_11/input.txt', 'r')
    lines = day11_input.readlines()
    seats = []

    for line in lines:
        row = line.rstrip('\n')
        seats.append([place for place in row])

    day11_input.close()
    return seats


if __name__ == "__main__":
    seats = get_seats()
    part_one_solution = count_occupied_seats(seats)

    print(f'The solution to part one is {part_one_solution}')
