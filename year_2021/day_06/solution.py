def simulate(get_input, days=80):
    population = [0 for _ in range(9)]

    for fish in next(get_input()).split(','):
        fish = int(fish)
        population[fish] += 1
    
    for _ in range(days):
        reproducers = population[0]
        population = population[1:] + [reproducers]
        population[6] += reproducers

    return sum(population)

def part_1(get_input):
    return simulate(get_input)

def part_2(get_input):
    return simulate(get_input, 256)