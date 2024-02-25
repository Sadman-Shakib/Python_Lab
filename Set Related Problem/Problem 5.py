"""
    you are given two sets of integers. write a function that takes two set and 
    if any element present both sets add it in ans list

    Sample input                    sample output                                       
    set1 = 2, 4, 6, 1, 8            8, 2
    set2 = 2, 8, 12, 0, 3
"""

#solution
set1 = {2, 4, 6, 1, 8}
set2 = {2, 8, 12, 0, 3}

def common_element(set1, set2):
    res = set()
    for i in set1:
        if i in set2:
            res.add(i)
    return res

print(common_element(set1, set2))