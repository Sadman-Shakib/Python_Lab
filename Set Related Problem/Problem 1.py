
# you are given a string(there will be no space in string). now your task is print the number 
# of unique charecters and all the unique charecters of strings


#  Sample Input                  Sample Output

#  masumbakaul                   7
#                                {'a', 's', 'k', 'l', 'b', 'm', 'u'}

#solution
s = "masumbakaul"

ans = set(s)

print(len(ans))

print(ans)