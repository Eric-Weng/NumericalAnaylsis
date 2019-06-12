#Eric Weng
#MATH 4650

#Homework 1 Bisection Method Implementation

import math

MAX_ITER = 19517
 
def func( x ): 
    return x + math.exp(x) 
  
# Prints root of func(x) in interval [a, b] 
def regulaFalsi( a , b): 
   
    iteration = 0

    if func(a) * func(b) >= 0: 
        print("You have not assumed right a and b") 
        return -1
      
    c = a # Initialize result 
      
    for i in range(MAX_ITER): 

        print("iteration:",iteration ," a:", a ," b:", b)

        # Find the point that touches x axis 
        c = (a * func(b) - b * func(a))/ (func(b) - func(a)) 
          
        # Check if the above found point is root 
        if func(c) == 0: 
            break
          
        # Decide the side to repeat the steps 
        elif func(c) * func(a) < 0: 
            b = c
            iteration += 1 
        else: 
            a = c 
            iteration += 1
    print("The value of root is : " , '%.4f' %c)
    print(iteration)
  
# Driver code to test above function 
# Initial values assumed 
a =-10
b = 10
regulaFalsi(a, b) 