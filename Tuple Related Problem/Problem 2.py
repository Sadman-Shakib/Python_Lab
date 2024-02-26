"""
    you are given two tuple concatanate those two tuples and print the sum of values

    Sample Input                              Sample Output

    5, 2, 4, 2, 4                                7
    7, 3, 5, 1, 9

"""

#solution

t1 = (5, 2, 4, 2, 4)
t2 = (7, 3, 5, 1, 9)

ans = tuple(t1 + t2)

print(sum(ans))