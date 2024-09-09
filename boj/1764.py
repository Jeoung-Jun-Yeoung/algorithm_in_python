import sys


n, m = map(int, sys.stdin.readline().strip().split())

# n 은 듣도 못한 사람
# m 은 보도 못한 사람
noLisitien = set()
noSee = set()

total = []
for _ in range(n):
    noLisitien.add(sys.stdin.readline().strip())

for _ in range(m):
    noSee.add(sys.stdin.readline().strip())

a = noSee.intersection(noLisitien)
a = list(a)
a.sort()
print(len(a))
for i in a:
    print(i)
