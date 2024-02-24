# you are given two list of integrs with same sizes (same length) 
# now create a new list with sum of every position values

# Sample Input                  Sample Output

# [3, 1, 7, 6]                  5, 9, 10, 10
# [2, 8, 3, 4]


#solution
list1 = [3, 1, 7, 6]
list2 = [2, 8, 3, 4]

res = list()

for i in range(0, len(list1)):
    res.append(list1[i] + list2[i])

print(res)
