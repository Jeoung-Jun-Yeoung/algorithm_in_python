from itertools import combinations


N, M = map(int, input().split())

houses = []
chickens = []

for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))

ans = 2 * N * len(houses)


def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


for combi in combinations(chickens, M):
    tot = 0
    # 생존 치킨집 조합 좌표를 뽑는다.
    for house in houses:
        # 집을 하나 고른다.
        tot += min(get_dist(house, chicken) for chicken in combi)
        # 치킨집좌표 조합을 하나씩 꺼내와서 각 집과의 거리를 비교
        # 가장 가까운 치킨집을 min을 통해 얻어옴
        # 가장 작은 값의 의미는 해당 집에서 가장 가까운 치킨집
        # 해당 값을 이번 조합에서의 최단거리이기에 토탈에 더해줌
        # 그담에 다음집을 봄.
        # 이렇게 반복하면 해당 치킨집을 뽑았을떄 각 집마다 가장 가까운거리가 나온다.
    ans = min(ans, tot)
print(ans)
