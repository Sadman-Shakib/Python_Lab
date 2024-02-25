"""
    you are given some unique integers . now your task is implement a function that 
    takes a sequences and an integer as parameter and return sum of first n smallest
    element 

    sample input                        sample output

    sequence = 2, 1, 3, 4, 0, 5         3     
    n = 3
     
"""

#solution

def fun(arr, n):
    st = set(arr)
    ls = list(st)
    return sum(ls[:n])

a = [2, 1, 3, 4, 0, 5]

print(fun(a, 3))