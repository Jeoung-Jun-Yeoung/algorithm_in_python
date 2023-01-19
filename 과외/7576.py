from collections import deque

import sys
sys.setrecursionlimit(10**6)

# 재귀 문제는 pypy보다 python 재출을 권장


def solve(A):
    N, M = len(A), len(A[0])
    # 편의상 선언
    # vis = [[False] * M for i in range(N)]

    dis = [[-1] * M for i in range(N)]
    # 한번도 방문 안했으면 -1 이고 방문했다면 해당 거리가 들어있음. vis와 역할기 곂침

    Q = deque()

    for i in range(N):
        for j in range(M):
            if A[i][j] == 1:
                Q.append((i, j))
                dis[i][j] = 0
    while len(Q) != 0:
        x, y = Q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = x + dx, y + dy
            if 0 <= r < N and 0 <= c < M and A[r][c] != -1 and dis[r][c] == -1:
                # 올바른 칸인지 확인
                Q.append((r, c))
                dis[r][c] = dis[x][y] + 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] == 0 and dis[i][j] == -1:
                return -1
            ans = max(ans, dis[i][j])
    return ans


def DFS(G, start):
    res, vis = [], [False] * len(G)

    def rec(v):
        vis[v] = True
        # 방문할때 vis에 들어간다.
        res.append(v)
        for u in G[v]:
            if not vis[u]:
                rec(u)
    rec(start)
    return res


def BFS(G, start):
    res, vis = [], [False] * len(G)

    Q = deque([start])
    # Q에 한번이라도 들어간 적이 있으면 vis에 들어간다.
    vis[start] = True
    while len(Q) != 0:

        v = Q.popleft()
        res.append(v)

        for u in G[v]:
            if not vis[u]:
                vis[u] = True
                Q.append(u)
    return res


def main():
    M, N = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    print(solve(A))


if __name__ == '__main__':
    main()
