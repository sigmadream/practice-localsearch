from numeric import *

EPSILON = 0.0001


def gradient(current, p, value, epsilon):
    gradient = []
    low = p[1][1]
    up = p[1][2]
    for i in range(len(current)):
        value = current[i]
        derivate = current[:i]
        if low[i] <= value + epsilon <= up[i]:
            value = value + epsilon
        derivate.append(value)
        derivate.extend(current[i + 1 :])
        gradient.append((evaluate(derivate, p) - value) / epsilon)
    return gradient


def gradient_descent(p):
    current = random_init(p)
    value = evaluate(current, p)
    while True:
        gradient_lst = gradient(current, p, value, EPSILON)
        next_p = take_step(gradient_lst, current)
        next_n = evaluate(next_p, p)
        if next_n <= value:
            value = next_n
            current = next_p
        else:
            break
    return (current, value)


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
