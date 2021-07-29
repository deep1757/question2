from collections import defaultdict
import math
from sys import stdin,stdout
for _ in range(int(input())):
    a=[]
    for i in range(3):
        a.append(list(map(int,input().split())))
    a.sort()
    f=0
    for i in range(1,3):
        if a[i][0]>=a[i-1][0] and a[i][1]>=a[i-1][1] and a[i][2]>=a[i-1][2] and not(a[i][0]==a[i-1][0] and a[i][1]==a[i-1][1] and a[i][2]==a[i-1][2]):
            continue
        else:
            f=1
            break
    if f:
        print("no")
    else:
        print("yes")