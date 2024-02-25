"""
    declare two string variable and count frequency of each charecter individually
    then take any charecter that is present both string at least one
    and then check if the frequency of this charecter in both string is same or not

    sample input                      sample output 

    masumbakaul                       Yes
    bakaulmasum

    rahim                             No
    kaaaarim


"""

# solution
a = "masumbakaul"
b = "bakaulmasum"

cntA = dict()
cntB = dict()

for i in a:
    if i in cntA:
        cntA[i] += 1
    else :
        cntA[i] = 1

for i in b:
    if i in cntB:
        cntB[i] += 1
    else :
        cntB[i] = 1

if cntA['a'] == cntB['a']:
    print("Yes")
else :
    print("No")
