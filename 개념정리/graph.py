import sys
from collections import deque
from collections import deque

sys.setrecursionlimit(10**6)


def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for next in range(1, N + 1):
        if not visited[next] and graph[idx][next]:
            # 방문은 안했지만, 길이 있다면 간다.
            dfs(next)


def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)


input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [[False] * (N + 1)]
# 양방향 체크를 안해줘도 되는건가?

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


dfs(V)
print()
visited = [False] * (N + 1)

q = [V]
visited[V] = True
bfs(V)
