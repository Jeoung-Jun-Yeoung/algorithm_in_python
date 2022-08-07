import sys

input = sys.stdin.readline

N, K = map(int, input().split())

Coin = [int(input()) for _ in range(N)]

Coin.sort(reverse=True)
rst = 0

for i in Coin:
    if K // i != 0:
        rst += K // i
        K = K % i
    if K == 0:
        break


print(rst)
