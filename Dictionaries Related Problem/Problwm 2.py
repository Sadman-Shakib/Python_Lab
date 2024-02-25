"""
    you are given a result of a section
    now your task is print the grade and count of each grade

    Sample Input                                    sample ouutput

    list = ["A+", "A", "A-", "A+", "B-", "A+"]      'A+': 3, 'A': 1, 'A-': 1, 'B-': 1
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

print(cnt)