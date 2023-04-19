from numeric import *

EPSILON = 0.0001


def gradient(current, p, values, epsilon):
    gradient = []
    low = p[1][1]
    up = p[1][2]
    for i in range(len(current)):
        values = current[i]
        derivate = current[:i]
        if low[i] <= values + epsilon <= up[i]:
            values = values + epsilon
        derivate.append(values)
        derivate.extend(current[i + 1 :])
        gradient.append((evaluate(derivate, p) - values) / epsilon)
    return gradient


def gradient_descent(p):
    current = random_init(p)
    values = evaluate(current, p)
    while True:
        gradient_lst = gradient(current, p, values, EPSILON)
        next_p = take_step(gradient_lst, current)
        next_n = evaluate(next_p, p)
        if next_n <= values:
            values = next_n
            current = next_p
        else:
            break
    return (current, values)


def take_step(gradient, current):
    suc = []
    for i in range(len(current)):
        suc.append(current[i] - (ALPHA * gradient[i]))
    return suc


def display_setting():
    print()
    print("Search algorithm: Gradient Descent")
    print()
    print("Update rate: ", ALPHA)
    print("Increment for calculating derivatives:", EPSILON)


if __name__ == "__main__":
    p = create_problem("./data/Griewank.txt")
    current, values = gradient_descent(p)
    display_setting()
    display_result(current, values)
