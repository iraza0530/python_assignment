
# 1)  Write a decorator to find the execution time of any function.
# 2)  Find 1001 members of Fibonacci series. Use the above created time execution calculator. (Try to optimize it).



import time
import math
 

def calculate_execution_time(func):
       
    def inner1(*args, **kwargs):
 
        begin = time.time()
         
        func(*args, **kwargs)
 
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
 
    return inner1
 
 
 

@calculate_execution_time
def find_factorial(num): 
    print("Factorial of number ",num, math.factorial(num))
 
find_factorial(1001)