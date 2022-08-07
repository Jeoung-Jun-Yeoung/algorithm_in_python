import sys
from itertools import combinations

input = sys.stdin.readline

dwarf = []
rst = ()

dwarf = [int(input()) for _ in range(9)]
# 이렇게 입력 받아도 된다.


for i in combinations(dwarf, 7):
    if sum(i) == 100:
        rst = tuple(sorted(i, key=lambda x: x))

for i in rst:
    print(i)


# from intertools import combinations
# dwarf = [int(input()) for _ in range(9)]
# for combi in combinations(dwarf, 7):
#       if sum(combi) == 100:
#           for dwarf in sorted(combi):
#               print(dwarf)
#           break
# 이렇게 짜면 여러개인 경우 여러번 다 출력됨.
