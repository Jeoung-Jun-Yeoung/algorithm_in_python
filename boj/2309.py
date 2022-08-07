import imp
import sys
from itertools import combinations

input = sys.stdin.readline

dwarf = []
rst = ()

for i in range(9):
    dwarf.append(int(input()))

for i in combinations(dwarf, 7):
    if sum(i) == 100:
        rst = tuple(sorted(i, key=lambda x: x))

for i in rst:
    print(i)
