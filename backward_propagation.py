learning_rate = 0.005


def f(x, a, b, c):
    return a * x ** 2 + b * x + c


def f_derivative_a(x):
    return x ** 2


def f_derivative_b(x):
    return x


def f_derivative_c():
    return 1


def error_pente_iteration(a, b, c):
    point = [[2, 11], [5, 13], [7, 16]]


def error_pente(a, b, c):
    x1 = 2
    x2 = 5
    x3 = 7

    f_vrai1 = 11
    f_vrai2 = 13
    f_vrai3 = 16

    f1 = f(x1, a, b, c)
    f2 = f(x2, a, b, c)
    f3 = f(x3, a, b, c)

    pente_a1 = f_derivative_a(x1)
    pente_a2 = f_derivative_a(x2)
    pente_a3 = f_derivative_a(x3)

    pente_b1 = f_derivative_b(x1)
    pente_b2 = f_derivative_b(x2)
    pente_b3 = f_derivative_b(x3)

    pente_c1 = f_derivative_c()
    pente_c2 = f_derivative_c()
    pente_c3 = f_derivative_c()

    gradient_a = 2 * (f1 - f_vrai1) * pente_a1 + 2 * (f2 - f_vrai2) * pente_a2 + 2 * (f3 - f_vrai3) * pente_a3
    gradient_b = 2 * (f1 - f_vrai1) * pente_b1 + 2 * (f2 - f_vrai2) * pente_b2 + 2 * (f3 - f_vrai3) * pente_b3
    gradient_c = 2 * (f1 - f_vrai1) * pente_c1 + 2 * (f2 - f_vrai2) * pente_c2 + 2 * (f3 - f_vrai3) * pente_c3

    print(a, b, c, gradient_a, gradient_b, gradient_c)
    if abs(gradient_a) + abs(gradient_b) + abs(gradient_c) < 1:
        return a, b, c

    if abs(gradient_a) > abs(gradient_b) and abs(gradient_a) > abs(gradient_c):
        if gradient_a < 0:
            return error_pente(a + learning_rate, b, c)
        else:
            return error_pente(a - learning_rate, b, c)

    if abs(gradient_b) > abs(gradient_a) and abs(gradient_b) > abs(gradient_c):
        if gradient_b < 0:
            return error_pente(a, b + learning_rate, c)
        else:
            return error_pente(a, b - learning_rate, c)

    if abs(gradient_c) > abs(gradient_a) and abs(gradient_c) > abs(gradient_b):
        if gradient_c < 0:
            return error_pente(a, b, c + learning_rate)
        else:
            return error_pente(a, b, c - learning_rate)


best_a, best_b, best_c = error_pente(5, -92 / 12, -14)
print(best_a, best_b, best_c)
