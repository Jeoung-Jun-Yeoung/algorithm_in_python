import sys

input = sys.stdin.readline

N, K = map(int, input().split())

Coin = [int(input()) for _ in range(N)]

# Coin.sort(reverse=True)
Coin.reverse()
# 반대로 정렬이 아니라 그냥 뒤집기만 해도 된다.
rst = 0

for i in Coin:
    if K // i != 0:
        rst += K // i
        K = K % i
    if K == 0:
        break


print(rst)
