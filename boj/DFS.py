# 정점이 13개
adj = [[0] * 13 for _ in range(13)]

adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
# .. 나머지는 생략
# for row in adj:
#     print(row)


# now -> 현재 방문한 노드.
def dfs(now):
    for nxt in range(13):
        # nxt는 다음 방문할 노드
        if adj[now][nxt]:
            dfs(nxt)
            # 방문할 노드의 간선이 존재하면 방문한다.


dfs(0)
