# 연결이 가장 많이 되어 있는 컴퓨터를 찾는다.
# 이후 해당컴퓨터가 신뢰하는 컴퓨터를 해킹한다.
# 이렇게 풀 면 될듯 하다.


N, M = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]


for i in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1
    print(A, B)
print(*graph)
