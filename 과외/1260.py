from collections import deque

import sys
sys.setrecursionlimit(10**6)

# 재귀 문제는 pypy보다 python 재출을 권장


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
    N, M, V = map(int, input().split())

    # 자신과 인접한 노드를 관리. 연결되어 있는 노드를 다 알려준다. G[1] -> 1번과 연결되어있는 것을 알려준다.
    G = [[] for i in range(N+1)]

    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        # 양방향방식. 단방향인 경우에는 한쪽만 넣어야 한다.

    for i in range(1, N+1):
        G[i].sort()

    print(*DFS(G, V))
    print(*BFS(G, V))


if __name__ == '__main__':
    main()
