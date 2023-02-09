from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end='')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True
    while queue:
        cur = queue.popleft()
        print(cur, end='')

        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def main():
    visited = [False] * 9
    dfs()
    bfs()


if __name__ == '__main__':
    main()
