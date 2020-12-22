
def largest_seat_id():
    day05_input = open('./2020/day_05/input.txt', 'r')
    lines = day05_input.readlines()
    largest_seat_id = float('-inf')

    for line in lines:
        seat = line.rstrip('\n')

        r_start, r_end = 0, 127
        c_start, c_end = 0, 6

        for i in range(0, 7):
            r_start, r_end = halve_seats(r_start, r_end, seat[i])
        for i in range(7, 10):
            c_start, c_end = halve_seats(c_start, c_end, seat[i])

        seat_id = r_start * 8 + c_start
        largest_seat_id = max(largest_seat_id, seat_id)

    day05_input.close()

    return largest_seat_id


def halve_seats(start, stop, direction):
    middle = (stop + start) // 2

    if direction in ['F', 'L']:
        return start, middle
    else:
        return middle + 1, stop


if __name__ == "__main__":
    part_one_solution = largest_seat_id()

    print(f'The solution to part one is {part_one_solution}')
