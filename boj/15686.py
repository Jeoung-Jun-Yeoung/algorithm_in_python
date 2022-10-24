from itertools import combinations
import copy

N, M = map(int, input().split())

maps = [input().replace(" ", "") for _ in range(N)]
chicken = []


for i in range(N):
    for j in range(N):
        if maps[i][j] == "2":
            chicken.append((i, j))

# 전체 치킨가게중 M개를 뽑음 조합으로 뽑음. 순서가 상관 없으니까
# 없엘곳을 뽑는게 깔끔해보임..
print(len(chicken))

for v in combinations(chicken, abs(M - len(chicken))):
    test_map = copy.deepcopy(maps)
    close_list = []
    for i in range(abs(M - len(chicken))):
        print("each x y ", v[i][0], v[i][1])

        test_map[v[i][0]][v[i][1]] = "0"
        print("each x y ", v[i][0], v[i][1])
        close_list.append((v[i][0], v[i][1]))
        print()
        print(test_map)
        print()
    print(close_list)
    # 각각의 집부터 치킨집까지 탐색하면서 거리를 잰다.


print("chicken ", chicken)

# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2
