import numpy


def newtons_method(f, df, x, eps):
    while abs(f(x)) > eps:
        x -= f(x) / df(x)
        print('x: {} \tf(x): {} \tdf(x): {}'.format(x.__round__(4), f(x).__round__(4), df(x).__round__(4)))
    return x


def simple_iter_method(f, df, x0, eps):
    x = x0 - f(x0) / df(x0)
    #print('x:{} \tf(x):{}'.format(x, x0 - f(x0) / df(x0)))
    while abs(x0 - x) > eps:
        #print('x:{} \tf(x):{}'.format(x, x - f(x) / df(x)))
        x0, x = x, x - f(x) / df(x)
    return x


def trapeze_method(f, a, b, eps):
    def iteration(h):
        s = 0.5 * (f(a) + f(b))
        #print('(f({}) + f({})) / 2 = ({} + {}) / 2 = {}'.format(
        #    a.__round__(4), b.__round__(4), f(a).__round__(4), f(b).__round__(4), s.__round__(4)))
        x = a + h
        while x <= b - h:
            s += f(x)
            #print('x = {}, f(x) = {}'.format(x.__round__(4), f(x).__round__(4)))
            x += h
        #print('mean = ', (h * s).__round__(4))
        return h * s

    h = (b - a) / 2
    s1 = iteration(h)
    h /= 2
    while True:
        s2 = iteration(h)
        h /= 2
        if abs(s2 - s1) < eps:
            break
        s1 = s2
    return s2


def simpson_method(f, a, b, eps):
    def iteration(n):
        h = (b - a) / n
        s = f(a) + f(b)
        x = a + h
        for i in range(1, n):
            if i % 2 == 0:
                s += 2 * f(x)
                #print('x = {}, 2*f(x) = {}'.format(x.__round__(4), f(x).__round__(4)))
            elif i % 2 == 1:
                s += 4 * f(x)
                #print('x = {}, f(x) = {}'.format(x.__round__(4), f(x).__round__(4)))
            x += h

        #print('mean = ', (h/3 * s).__round__(4))
        return h / 3 * s

    n = 2
    s1 = iteration(n)
    n *= 2
    while True:
        s2 = iteration(n)
        n *= 2
        if abs(s2 - s1) < eps:
            break
        s1 = s2

    return s2


def task11func(a, b, A, B, n, p, q, f):
    h = (b - a) / n
    D0, D1 = A + h, h
    y = [[A, D0], [0, D1]]
    x = numpy.arange(a, b + h, h).round(3)

    def get_c1():
        return (B - y[0][-1]) / y[1][-1]

    def get_solv_y_i(i):
        return y[0][i] + get_c1() * y[1][i]

    def div(a, b):
        return a / b

    for i in range(1, n):
        y[0].append(
            div(
                (h ** 2 * f(x[i]) - (1.0 - (h / 2) * p(x[i])) * y[0][i - 1] - (h ** 2 * q(x[i]) - 2) * y[0][i]),
                1 + h / 2 * p(x[i])
            )
        )
        y[1].append(
            div(
                -(1 - h / 2 * p(x[i])) * y[1][i - 1] - (h ** 2 * q(x[i]) - 2) * y[1][i],
                1 + h / 2 * p(x[i])
            )
        )
        #print('y[0][{i}] = ({h}**2 * f({x_i}) - (1.0 - ({h}/2) * {y_0} - (({h}**2)*q({x_i}) - 2) * {y_1}) '
       #      '/ (1 + {h} / 2 * p({x_i}))'.format(i=i, h=h, x_i=x[i], y_0=y[0][i - 1].__round__(3),
       #                                          y_1=y[0][i].__round__(3)))
       # print('y[1][{i}] = (-(1 - {h}/2*p({x_i})) * {y_0} - {h}**2 * q({x_i} - 2) * {y_1}) '
        #     '/ (1 + {h}/2) * p({x_i}))'.format(i=i, h=h, x_i=x[i], y_0=y[1][i - 1].__round__(3),
        #                                        y_1=y[1][i].__round__(3)))

    solution = [get_solv_y_i(i) for i in range(n+1)]
    [print('{y_0:4f}\t{y_1:4f}\t{x_:4f}\t{y_:4f}'.
           format(y_0=y0, y_1=y1, x_=x_, y_=y_))
           for y0, y1, x_, y_ in zip(y[0], y[1], x, solution)]

    return x, solution


if __name__ == '__main__':
    print("Functions for solving f(x)")
    print("Newton method: ", newtons_method.__name__)
    print("By simple iterations: ", simple_iter_method.__name__)
    print('Solve defined integral in [a, b]', trapeze_method.__name__)
    print('Simpson method', simpson_method.__name__)
