"""
    you are given an list. now your task is find the most frequent element of the list
    if multiple element have same frequency print any of them

    sample input                      sample output

    2 3 4 5 2 4 2 2 1                 2
"""

#solution
arr = [2, 3, 4, 5, 2, 4, 2, 2, 1]
cnt = dict()
mx_cnt = 0
ans = arr[0]

for i in arr:
    if i in cnt:
        cnt[i] += 1
        if mx_cnt < cnt[i]:
            mx_cnt = cnt[i]
            ans = i
    else:
        cnt[i] = 1

print(ans)
