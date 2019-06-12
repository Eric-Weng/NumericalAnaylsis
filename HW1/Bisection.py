#Eric Weng
#MATH 4650

#Homework 1 Bisection Method Implementation

import math

def func(x): 
    return math.tan(x)
   

def bisection(a,b,tol): 

    i = 0

    # Check for good guesses
    if (func(a) * func(b) >= 0): 
        print("You have not assumed right a and b\n") 
        return
   
    c = a 
    while ((b-a) >= tol): 
  
        # Find middle point 
        c = (a+b)/2
        print("iteration:",i ," a:", a ," b:", b)
   
        # Check if middle point is root 
        if (func(c) == 0.0): 
            break
   
        # Decide the side to repeat the steps 
        if (func(c)*func(a) < 0): 
            b = c 
            i+=1
        else: 
            a = c 
            i+=1
              
    print("The value of root is : ","%.4f"%c)
      
a = 2
b = 4
bisection(a, b, 0.00001)