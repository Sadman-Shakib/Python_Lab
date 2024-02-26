"""
    you are given two list list1 and list2
    now your task is print the element which are not present in list 2 at least 2 times

    sample input                          sample output

    ls1 = [1, 2, 4, 5, 4, 8, 9]           1 2
    ls2 = [1, 1, 2, 2, 3, 4, 5, 6]

"""

#solution
ls1 = [1, 2, 4, 5, 4, 8, 9]
ls2 = [1, 1, 2, 2, 3, 4, 5, 6]

cnt = dict()
for i in ls2:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in ls1:
    if i not in cnt: continue
    if cnt[i] > 1:
        print(i, end = " ")
