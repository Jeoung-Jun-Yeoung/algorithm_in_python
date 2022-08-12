from collections import deque

adj = [[0] * 13 for _ in range(13)]

adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1


def bfs():
    dq = deque()
    # 덱을 만들어주고
    dq.append(0)
    # root를 넣어주면서 시작
    while dq:
        now = dq.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)


bfs()
