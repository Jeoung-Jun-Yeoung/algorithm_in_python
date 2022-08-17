import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, K = map(int, input().split())

MOD = 10007
cache = [[0] * 1001 for _ in range(1001)]

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
for i in range(7):
    print(cache[i])
print()

# 삼각수를 채우면 된다. 삼각형을 채우면 되는데 행렬은 직사각형 모양.. 즉 0,0만 필요하고 0,1000은 필요없음

# top - down 방식
# def bino(n, k):
#     if cache[n][k]:
#         return cache[n][k]
#     if k == 0 or k == n:
#         cache[n][k] = 1
#     else:
#         cache[n][k] = bino(n-1, k-1) + bino(n-1, k)
#         # cache[n][k] %= MOD
#     return cache[n][k]


print(cache[N][K] % MOD)
