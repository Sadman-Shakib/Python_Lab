"""

    you are given two tuples now your task is concatanate two tuples and print every odd 
    position values 

    Sample Input                         Sample Output
    
    (5, 2, 4, 2, 4)                      2 2 7 5 9                            
    (7, 3, 5, 1, 9)
"""

#solution
a = (5, 2, 4, 2, 4)                                
b = (7, 3, 5, 1, 9)
ans = a + b

for i in range(1, len(ans), 2):
    print(ans[i], end = " ")