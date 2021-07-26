from sys import stdin

n = int(stdin.readline())
bag = 0
weight = 0
real_n = n
flag = 0
temp = 0
while 1:
    if (n%5) == 0:
        print(n//5)
        break
    n = n - 3
    bag += 1
    if n < 0:
        print(-1)
        break