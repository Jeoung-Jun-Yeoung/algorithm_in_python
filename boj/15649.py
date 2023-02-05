from itertools import permutations


N, M = map(int, input().split())

co = [i for i in range(1, N + 1, 1)]
for j in permutations(co, M):
    print(*j)
