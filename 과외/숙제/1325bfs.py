from collections import deque

import sys

input = sys.stdin.readline


def bfs(V):
    q = deque([V])
    visited[V] = True
    global count
    global graph
    while q:
        cur = q.popleft()
        count += 1
        # 현재 나의 컴퓨터 번호
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
    return count


N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

countHak = [0 for i in range(N + 1)]

for i in range(1, N+1):
    count = 0
    visited = [False] * (N + 1)
    countHak[i] = bfs(i)
maxrst = max(countHak)

for i, val in enumerate(countHak):
    if maxrst == val:
        print(i, end=' ')
