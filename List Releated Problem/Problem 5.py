# in this problem you have given two list . now create a function that takes two list as parameter.
# now your task is return a sorted unique element in single line


# Sample Input                  Sample Output

# [13, 2, 2, 1]                 1, 2, 3, 7, 13
# [1, 2, 3, 7]


#solution
list1 = [13, 2, 2, 1]
list2 = [1, 2, 3, 7]

def unique_list(a, b):
    temp = set()
    for i in a:
        temp.add(i)
    for i in b:
        temp.add(i)
    return temp

print(unique_list(list1, list2))

