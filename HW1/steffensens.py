import math

accelerate = lambda x0, x1, x2: (x0*x2 - x1*x1)/(x0 + x2 - 2*x1)

def steffensens(f, p, TOL):
    error = 1
    i = 0
    while error > TOL:
        p1 = f(p)
        p2 = f(p1)
        p_new = accelerate(p, p1, p2)
        error = abs(p_new-p)
        i += 1
        print(f'P0: {p:.7f}\nP1: {p1:.7f}\nP2: {p2:.7f}\nP-hat_{i}: {p_new:.7f}\n')
        p = p_new
    print(f'Final value: {p}\nIterations: {i}')

if __name__ == '__main__':
    f = lambda x: (x*x*x)-25
    steffensens(f, 3, .0001)