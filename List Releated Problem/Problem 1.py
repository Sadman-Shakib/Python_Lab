# you are given a list of naturel integers numbers. now define a function that takes a list of integers as 
# parameter and return a list with only contains positive values

#  Sample Input                  Sample Output

#  [1, 2, -1, 5, -3, 3]          1, 2, 5, 3



#solution
num = [1, 2, -1, 5, -3, 3]

ans = list()

for i in num:
    if i >= 0:
        ans.append(i)

print(ans)