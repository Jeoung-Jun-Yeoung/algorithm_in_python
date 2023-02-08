from collections import deque
# 경로 찾기
# 실버 1


def bfs(V):
    global visited
    global Graph
    q = deque([V])
    # Graph를 보고 탐색하면서 rst_map을 채워나간다.
    while q:
        cur_node = q.popleft()

        for next in Graph[cur_node]:
            if not visited[next]:
                visited[next] = True
                q.append(next)


n = int(input())

G = []

for _ in range(n):
    line = list(map(int, input().split()))
    G.append(line)
    print(line)

Graph = [[] * n for _ in range(n)]
visited = [[False] * n]
rst_map = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if G[i][j] == 1:
            Graph[i].append(j)
            # 경로가 있다면
print(Graph)

bfs(0, rst_map)
