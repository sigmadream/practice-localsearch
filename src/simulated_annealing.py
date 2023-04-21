import math
import random
from numeric import *

EPSILON = 0.0001
LIMITS = 100
DELTA = 0.01
NUM_EXP = 1
LIMIT_EVAL = 5000
NUM_SAMPLE = 100

def random_mutant(current, p):
    i = random.randint(0, len(current) - 1)
    delta = [DELTA, -DELTA]
    d = random.choice(delta)
    return mutate(current, i, d, p)
        

def init_temp(p):
    diffs = []
    for i in range(NUM_SAMPLE):
        c0 = random_init(p)
        v0 = evaluate(c0,p)
        c1 = random_mutant(c0, p)
        v1 = evaluate(c1,p) 
        diffs.append(abs(v1 - v0))
    dE = sum(diffs) / NUM_SAMPLE
    t = dE / math.log(2)
    return t

def t_schedule(t):
    return t * (1 - (1 / 10**4))

        
def display_setting():
    print()
    print("Search Algorithm: Simulated Annealing")
    print()
    print(f"Mutation step size: {DELTA}")
    print()
    print(f"Number of evaluations until termination: {LIMIT_EVAL:,}")
    print()
    print(f"Number of Experiments: {NUM_EXP}")


def simulated_annealing(p):
    current = random_init(p)
    value = evaluate(current,p)
    best_current, best_value = current, value
    _whenBestFound = i = 1
    
    f = open('anneal.txt','w')
    t = init_temp(p)
    while True:
        f.write(str(value) + '\n')
        t = t_schedule(t)
        if t == 0 or i == LIMIT_EVAL:
            break
        neighbor = random_mutant(current,p)
        valueN = evaluate(neighbor,p)
        i+=1        
        if (valueN - value) < 0:
            current = neighbor
            value = valueN 
        elif random.uniform(0,1) < math.exp(-1*(valueN - value)/t):
            current = neighbor
            value = valueN
        if value < best_value:
            (best_current, best_value) = (current, value)
            whenBestFound = i
    _whenBestFound = whenBestFound                    
    f.close()
    return (best_current, best_value)


if __name__ == "__main__":
    p = create_problem("./data/Convex.txt")
    current, minimum = simulated_annealing(p)
    describe_problem(p)
    display_setting()
    display_result(current, minimum)

