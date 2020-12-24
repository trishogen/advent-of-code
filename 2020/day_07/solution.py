
def containing_shiny_gold(rules):
    bags_to_search_for = ['shiny gold']
    next_search = []
    solution = {}

    while bags_to_search_for:
        for k, v in rules.items():
            for bag in v:
                if bag in bags_to_search_for:
                    solution[k] = True
                    next_search.append(k)
                    break
        bags_to_search_for = next_search
        next_search = []

    return len(solution)


def read_in_rules():
    day07_input = open('./2020/day_07/input.txt', 'r')
    lines = day07_input.readlines()
    bags = {}

    for line in lines:
        rule = line.rstrip('\n')
        rule_split = rule[:-1].split(' contain ')
        bag = rule_split[0].split(' bags')[0]
        bags_contained = rule_split[1].split(', ')
        inside_bags = [bag.split(' ')[1] + ' ' + bag.split(' ')[2] for bag in bags_contained]
        bags[bag] = inside_bags

    day07_input.close()
    return bags


if __name__ == "__main__":
    rules = read_in_rules()
    part_one_solution = containing_shiny_gold(rules)

    print(f'The solution to part one is {part_one_solution}')
