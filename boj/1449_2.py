import sys
input = sys.stdin.readline
N, L = map(int, input().split())
Crak = list(map(int, input().split()))
# -> 좌표 압축.
Crak.sort()

taping = 0

i = 0
now = Crak.pop(0)
