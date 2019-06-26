import math

def func( x ): 
    return x*x*math.exp(math.pow(-x,2))
      
# Function to evalute the value of integral 
def trapezoidal (a, b, n): 
      
    # Grid spacing 
    h = (b - a) / n 
      
    # Computing sum of first and last terms 
    # in above formula 
    s = (func(a) + func(b)) 
  
    # Adding middle terms in above formula 
    i = 1
    while i < n: 
        s += 2 * func(a + i * h) 
        i += 1
          
    # h/2 indicates (b-a)/2n.  
    # Multiplying h/2 with s. 
    return ((h / 2) * s) 
  
# Driver code
lower_limit = 0
upper_limit = 2 
n = 8
print ("%.6f"%trapezoidal(lower_limit, upper_limit, n)) 