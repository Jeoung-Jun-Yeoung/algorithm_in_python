import sys


n, m = map(int, sys.stdin.readline().strip().split())

# n 은 듣도 못한 사람
# m 은 보도 못한 사람
noLisitien = []
noSeeAndLisiten = []

total = []
for _ in range(n + m):
    total.append(sys.stdin.readline().strip())


noLisitien = total[:n]
noSee = total[n+1:]


for li in noLisitien:
    if li in noSee:
        noSeeAndLisiten.append(li)

print(len(noSeeAndLisiten))
noSeeAndLisiten.sort()
for i in noSeeAndLisiten:
    print(i)
