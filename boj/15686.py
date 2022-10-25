from itertools import combinations
import copy

N, M = map(int, input().split())

maps = [list(input().replace(" ", "")) for _ in range(N)]

chicken = []
home = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == "2":
            chicken.append((i, j))
        elif maps[i][j] == "1":
            home.append((i, j))

# maps구현 끝

# 없엘곳을 뽑자.
# 없엔다음에 집 기준으로 찾자.

rst = []

# 치킨집을 기준으로 각 집에서 최단거리의 합을 업데이트
if M == 1:
    for v in combinations(chicken, M):
        # 생존한 치킨집을 뽑음
        for cx, cy in v:
            sd = []
            # 해당 치킨집의 좌표를 얻어서
            for x, y in home:
                d = abs(x - cx) + abs(y - cy)
                sd.append(d)
        rst.append(sum(sd))
    print(min(rst))
# 각 가정마다 어떤 치킨집이 생존했을때 최단거리인지를 갱신
else:
    sd = [2 * N for _ in range(len(home))]
    for v in combinations(chicken, M):

        # 생존한 치킨집을 뽑음
        for cx, cy in v:
            # 해당 치킨집의 좌표를 얻어서
            idx = 0
            for x, y in home:
                d = abs(x - cx) + abs(y - cy)
                if d < sd[idx]:
                    sd.pop(idx)
                    sd.insert(idx, d)
            # 각 집과의 거리를 계산해서 비교.
                idx += 1

        rst.append(sum(sd))
    print(min(rst))
