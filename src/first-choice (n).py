from numeric import *

LIMITS = 100


def first_choice(p):
    current = random_init(p)
    value = evaluate(current, p)
    i = 0
    while i < LIMITS:
        successor = random_mutant(current, p)
        eval_value = evaluate(successor, p)
        if eval_value < value:
            current = successor
            value = eval_value
            i = 0
        else:
            i += 1
    return current, value


def random_mutant(current, p):
    i = random.randint(0, len(current) - 1)
    delta = [DELTA, -DELTA]
    d = random.choice(delta)
    return mutate(current, i, d, p)


def display_setting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)


if __name__ == "__main__":
    p = create_problem("./data/Convex.txt")
    current, minimum = first_choice(p)
    describe_problem(p)
    display_setting()
    display_result(current, minimum)
