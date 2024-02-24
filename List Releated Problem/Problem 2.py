# you have given an array with intergers numbers 
# now your task is whenever you find number one you have to replace this with "Found 1"
# and last print the complete updated list 

#  Sample Input                  Sample Output

#  [1, 2, 3, 4, 5, 2, 1, 3]      ['Found One', 2, 3, 4, 5, 2, 'Found One', 3] 



#solution 
arr = [1, 2, 3, 4, 5, 2, 1, 3]

for i in range(0, len(arr)):
    if arr[i] == 1:
        arr[i] = "Found One"

print(arr)


