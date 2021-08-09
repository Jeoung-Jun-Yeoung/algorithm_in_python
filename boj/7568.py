# 리스트 
from sys import stdin

t = int(stdin.readline())

arr = []
rst = []
for i in range(t):
    w,h = map(int,stdin.readline().split())
    arr.append([w,h])
for i in arr:
    temp = 1
    for j in arr:
        if j[0] > i[0] and j[1] > i[1]:
            temp += 1
    rst.append(str(temp))

print(" ".join(rst))
