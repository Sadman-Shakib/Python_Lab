# you are given a list of integers . now your task is build a new list using 
# list comprehension technique so that new list only contains positive values


#  Sample Input                  Sample Output

#  [1, 2, -1, 5, -3, 3]          1, 2, 5, 3


#solution
num = [1, 2, -1, 5, -3, 3]

ans = [values for values in num if values > 0]

print(ans)