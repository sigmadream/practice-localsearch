from tsp import *


def steepest_ascent(p):
    current = random_init(p)
    value = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, best_of_value) = best_of(neighbors, p)
        if best_of_value >= value:
            break
        else:
            current = successor
            value = best_of_value
    return (current, value)


def mutants(current, p):
    n = p[0]
    neighbors = []
    count = 0
    tried_pairs = []
    while count <= n:
        i, j = sorted([random.randrange(n) for _ in range(2)])
        if i < j and [i, j] not in tried_pairs:
            tried_pairs.append([i, j])
            current_copy = inversion(current, i, j)
            count += 1
            neighbors.append(current_copy)
    return neighbors


def best_of(neighbors, p):
    all = []
    for i in range(len(neighbors)):
        all.append(evaluate(neighbors[i], p))
    best_value = min(all)
    best = neighbors[all.index(best_value)]
    return (best, best_value)


def display_setting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")


if __name__ == "__main__":
    p = create_problem("./data/tsp30.txt")
    current, minimum = random_init(p)
    describe_problem(p)
    # display_setting()
    # display_result(current, minimum)
