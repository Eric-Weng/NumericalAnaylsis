#Eric Weng
#MATH 4650

#Homework 1 Bisection Method Implementation

import math

def func( x ): 
    return x+math.exp(x)
  
# Derivative of the above function  
def derivFunc( x ): 
    return math.exp(x)+1
  
# Function to find the root 
def newton( x ): 
    i = 0
    h = func(x) / derivFunc(x) 
    while abs(h) >= 0.0001: 
        h = func(x)/derivFunc(x) 
          
        # x(i+1) = x(i) - f(x) / f'(x) 
        x = x - h 
        i+=1
        print("Iterations:",i, "x:", x)

    print("The value of the root is : ","%.4f"% x) 
  
# Driver program to test above 
x0 = 5 # Initial values assumed 

newton(x0) 