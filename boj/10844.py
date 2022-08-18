import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(9)

else:
    temp = 2 ** (N-1)
    print(temp * 8 + 1)
