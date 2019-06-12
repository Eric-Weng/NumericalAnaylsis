#Eric Weng
#MATH 4650

#Homework 1 Secant Method Implementation
    
import math

def secant(f, x1, x2, TOL):
    error = 1
    iterations = 0
    print(f'x0: {x1}\nx1: {x2}')
    while error > TOL:
        x_new = x2 - (f(x2)*(x2-x1))/(f(x2)-f(x1))
        error = abs(x_new - x2)
        x1 = x2
        x2 = x_new
        iterations += 1
        print(f'x{iterations+1}: {x2}')
    print(f'Result: {x2}\nIterations: {iterations}')

if __name__ == '__main__':
    f = lambda x: x + math.exp(x)
    secant(f, -10, 10, 0.0001)