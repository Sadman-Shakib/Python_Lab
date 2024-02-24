"""
 you are given a list . first print all values from middle to end and then
 middle to front in reverse order 

 sample input                     sample output

 [1, 2, 4, 5, 6, 7, 8, 9]         [6, 7, 8, 9] [5, 4, 2, 1]
"""

x = [1, 2, 4, 5, 6, 7, 8, 9]

sz = len(x)

print(x[sz // 2 :], end = " ")

rev = x[ : -sz // 2]

rev.reverse()

print(rev)