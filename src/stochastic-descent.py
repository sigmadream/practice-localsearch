import random
from numeric import *

EPSILON = 0.0001
LIMITS = 100
DELTA = 0.01

def stochastic_best(neighbors, p):
    Min = [evaluate(x,p) for x in neighbors]
    Max = [max(Min) + 1 - x for x in Min]    
    rand = random.uniform(0,len(Max))
    s = Max[0]    
    for i in range(len(Max)):
        if rand<=s :
            break
        else:
            s += Max[i+1]
    return neighbors[i], Min[i]

def stochastic_gradient_descent(p):
    current = random_init(p)
    value = evaluate(current,p)
    i = 0
    while i < LIMITS:
        neighbors = mutants(current)
        successor, best_of_value = stochastic_best(neighbors,p)
        if best_of_value < value:
            current = successor
            value = best_of_value
            i = 0
        else:
            i += 1
    return current, value

def mutants(current):
    neighbors = []
    for i in range(0,len(current)):
        neighbors.append(mutate(current, i, DELTA, p))
        neighbors.append(mutate(current, i, -DELTA, p))
    return neighbors

def display_setting():
    print()
    print("Search Algorithm: Stochastic Hill Climbing")
    print()

if __name__ == "__main__":
    p = create_problem("./data/Convex.txt")
    current, minimum = stochastic_gradient_descent(p)
    describe_problem(p)
    display_setting()
    display_result(current, minimum)
