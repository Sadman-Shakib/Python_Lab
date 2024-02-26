"""

    in this task you are given two world cup group one is latin america group 
    another one is europe teams. each team of same group will play every team of another 
    groups team. now create a match fixture (all possible match). for combaine 
    every pair of match use tuple



    Sample Input                 Sample Output

     ["arg", "brazil"]           ('arg', 'eng') ('arg', 'fra') ('brazil', 'eng') ('brazil', 'fra')

     ["eng", "fra"]
"""

grp1 = ["arg", "brazil"]
grp2 = ["eng", "fra"]

for i in grp1:
    for j in grp2:
        tp = (i, j)
        print(tp, end = " ")

