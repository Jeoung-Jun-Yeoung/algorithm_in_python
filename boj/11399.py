from sys import stdin

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
arr.sort()
be = 0
rst = 0
for i in arr:
    be = be + i
    rst = rst + be
print(rst)