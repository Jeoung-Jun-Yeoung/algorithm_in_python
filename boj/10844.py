import sys

input = sys.stdin.readline
MOD = 1000000000
N = int(input())

if N == 1:
    print(9)
if N == 2:
    print(17)
else:
    nine = N - 1
    eight = N
    other = (N + 1) * 7
    print(nine + eight + other % MOD)
