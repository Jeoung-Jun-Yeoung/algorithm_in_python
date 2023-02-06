# 연결이 가장 많이 되어 있는 컴퓨터를 찾는다.
# 이후 해당컴퓨터가 신뢰하는 컴퓨터를 해킹한다.
# 이렇게 풀 면 될듯 하다.

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**4 + 100)


def dfs(V):
    visited[V] = True
    global count
    # graph[A] -> node 값이 들어있음
    for i in graph[V]:
        # print(f'v {V} ->  i {i}')
        if not visited[i]:
            dfs(i)
            count += 1
    return count


N, M = map(int, input().split())

graph = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)
countHak = [0 for i in range(N + 1)]
# print(graph)
# print(countHak)

for i in range(1, N + 1):
    count = 1
    visited = [False] * (N + 1)
    countHak[i] = dfs(i)

maxrst = max(countHak)

for i, val in enumerate(countHak):
    if maxrst == val:
        print(i, end=' ')
