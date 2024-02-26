"""

    you are given two tuple define a function where fucntion takes two tuple as 
    parameter and return middle value of tuple if we concatanate those two tuples

    Sample Input                                 Sample Output
    
    5, 2, 4, 2, 4                                7
    5, 2, 4, 2, 4
"""

#solution
def getMid(x, y):
    temp = tuple()
    temp = x + y
    return temp[len(temp) // 2]

t1 = (5, 2, 4, 2, 4)
t2 = (7, 3, 5, 1, 9)

print(getMid(t1, t2))