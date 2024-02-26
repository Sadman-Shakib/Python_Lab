"""
    you are given a result of a section
    now your task is count number of student whos grade point is A+

    Sample Input                                    sample ouutput

    list = ["A+", "A", "A-", "A+", "B-", "A+"]      
"""

#solution
ls = ["A+", "A", "A-", "A+", "B-", "A+"]
cnt = dict()
ans = 0

for i in ls:
    if i in cnt:
        cnt[i] += 1
    else :
        cnt[i] = 1

print(cnt["A+"])