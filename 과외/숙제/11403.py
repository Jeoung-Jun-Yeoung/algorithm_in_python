from collections import deque
# 경로 찾기
# 실버 1


def bfs(V):
    global visited
    global Graph
    q = deque()
    # Graph를 보고 탐색하면서 rst_map을 채워나간다.
    for i in Graph[V]:
        q.append(i)
        visited[i] = True

    while q:

        cur_node = q.popleft()
        rst_map[V][cur_node] = 1

        for next in Graph[cur_node]:
            # print(f'next {next}')
            if not visited[next]:
                # next -> 갈수있는것도 넣어준다?
                visited[next] = True
                # 여기를 고정하면 V에서부터 갈수 있는 모든걸 다 1로 체크가 됨.
                q.append(next)


n = int(input())

G = []

for _ in range(n):
    line = list(map(int, input().split()))
    G.append(line)

Graph = [[] * n for _ in range(n)]

rst_map = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if G[i][j] == 1:
            Graph[i].append(j)

            # 0 -> 1
            # 1 -> 2
            # 2 -> 0
            # 경로가 있다면

for i in range(n):
    visited = [False] * n
    bfs(i)

for t in rst_map:
    print(*t)
