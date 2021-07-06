# from collections import deque

a = int(input())
b = int(input())
c = int(input())

rst = str(a*b*c)

li = dict()

# li[3] = value(값)

li = {"0" : 0, "1" : 0, "2" : 0, "3" : 0,"4" : 0,"5" : 0,"6" : 0,"7" : 0,"8" : 0,"9" : 0}


for i in rst:
   li[i] += 1

for i in li.values():
    print(i)