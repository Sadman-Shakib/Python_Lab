"""

    you are given a tuple. now your task is using Tuple Comprehensive
    write a code where you have to remove 
    every even element. after removing even element print this values as tuples.
    
    Use Tuple Comprehensive

    Sample Input                      Sample Output

    (2, 1, 2, 4, 5, 2, 7, 8)          (1, 5, 7)
"""

#solution
tp = (2, 1, 2, 4, 5, 2, 7, 8)

ans = tuple(i for i in tp if i % 2 == 1)

print(ans)