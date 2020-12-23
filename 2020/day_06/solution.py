
def answered_yes():
    day06_input = open('./2020/day_06/input.txt', 'r')
    lines = day06_input.readlines()
    count = 0
    questions = {}

    for line in lines:
        person = line.rstrip('\n')
        if not person:
            count += len(questions)
            questions = {}
        for answer in person:
            questions[answer] = True

    count += len(questions)
    day06_input.close()

    return count


if __name__ == "__main__":
    part_one_solution = answered_yes()

    print(f'The solution to part one is {part_one_solution}')