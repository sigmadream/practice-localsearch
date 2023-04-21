from numeric import *


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
    neighbors = []
    for i in range(0, len(current)):
        neighbors.append(mutate(current, i, DELTA, p))
        neighbors.append(mutate(current, i, -DELTA, p))
    return neighbors


def best_of(neighbors, p):
    all = []
    for i in range(0, len(neighbors)):
        all.append(evaluate(neighbors[i], p))
    best_value = min(all)
    best = neighbors[all.index(min(all))]
    return (best, best_value)


def display_setting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)


if __name__ == "__main__":
    p = create_problem("./data/Convex.txt")
    current, minimum = steepest_ascent(p)
    describe_problem(p)
    display_setting()
    display_result(current, minimum)
