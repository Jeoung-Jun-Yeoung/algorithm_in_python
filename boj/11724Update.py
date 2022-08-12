import sys

input = sys.stdin.readline

N, M = map(int, input().split())
check = [False] * N
adj = [[False] * N for _ in range(N)]

for _ in range(M):
    x, y = map(lambda x: x - 1, map(int, input().split()))
    adj[x][y] = adj[y][x] = True

# for row in adj:
#     print(row)
# test 출력용


def dfs(now):
    for next in range(N):
        if adj[now][next] and not check[next]:
            check[next] = True
            dfs(next)

# 방문전에 체크하는것이 최적화에 더 좋다.


cnt = 0
for i in range(N):
    if not check[i]:
        check[i] = True
        cnt += 1
        dfs(i)

print(cnt)
