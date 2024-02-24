# you are given a set of integers {1, 2, 3, 4, 5} , write a Python program to add a new integer in set,
# first take a integers input and if it present in set print "Already present".
# otherwise add in set and print the set

#  Sample Input                  Sample Output

#  2                             Already present 
#  8                             1, 2, 3, 4, 5, 8                           

#solution

present = {1, 2, 3, 4, 5}

n = int(input())

if n in present:
    print("Already present")
else :
    present.add(n)
    print(present)