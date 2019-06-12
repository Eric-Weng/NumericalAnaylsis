#Eric Weng
#MATH 4650

#Homework 1 FPI Method Implementation

import math

def fixed_point_iteration(f, p, TOL):
    error = 1
    iterations = 0
    while error > TOL:
        p_new = f(p)
        error = abs(p_new - p)
        p = p_new
        iterations += 1
        print(f'p{iterations} = {p: 0.5f}')
    print(f'Root: {p}\nIterations: {iterations}')

if __name__ == '__main__':
    f = lambda x: 2*math.sin(math.pi*x)+x
    fixed_point_iteration(f, 1, 0.0001)