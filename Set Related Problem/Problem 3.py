"""Exam Paper
you are given a set {1, 2, 3, 4, 5} and a list  [1, 2, 3] remove all integers from set that is present in the list


  Sample Input                        Sample Output

                                      4, 5
"""

s = {1, 2, 3, 4, 5}

num = [1, 2, 3]

for i in num:
    if i in s:
        s.remove(i)

print(s)