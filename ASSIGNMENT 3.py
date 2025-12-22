#TASK_1

def fact_rec(num):
    if num == 1:
        return 1
    else:
        factorial=num*fact_rec(num-1)
        return factorial

n=int(input("Enter a number: "))
print(f"Factorial Number of {n} is: {fact_rec(n)}")

#TASK_2

import math

n=int(input("Enter a number: "))

print(f"Square root of {n} is: {math.sqrt(n)}")
print(f"Logarithm of {n} is: {math.log(n)}")
print(f"Sine of {n} is: {math.sin(n)}")