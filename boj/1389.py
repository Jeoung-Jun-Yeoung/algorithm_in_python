from collections import deque

N, M = map(int, input().split())

rel = [[0] * N for _ in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    x = x - 1
    y = y - 1
    rel[x][y] = 1
    rel[y][x] = 1

# 입출력 받는걸 너무 못한다. 일단 입력받는거부터 너무 못함

# 1번째 오류 : 친구사이는 중복으로 표시해주어야 한다. 양방향 연걸이니까..
# x -= 1이거 은근 오류가 많은듯

# print(rel)
# print()
# print()


def bfs(start):
    chk = [False for _ in range(N)]
    # print("chk ", chk)

    # check 배열 만드는거 연습좀 잘해보자.. 이건 좌표별이 아니라 노드기준이니까 1차원 체크배열이면 됌
    # print("chk ", chk)

    tot = 0
    q = deque()
    d = 0
    # 시작점 넣고, 노드별로 총합도 구해야하니까 큐에 같이넣어준다.
    q.append((start, d))
    # 방문여부 체크해주는거 외우기
    chk[start] = True

    while q:
        s, nd = q.popleft()
        for nxt in range(N):
            temp = nd
            # 나랑 친구고, 방문안했으면 가본다.
            if rel[s][nxt] == 1 and not chk[nxt]:
                chk[nxt] = True
                # 방문여부 체크해주고 한친구에게 갓으니까 거리값 1올려줌
                nd = nd + 1
                # 토탈에 더해줌
                tot += nd
                q.append((nxt, nd))
            # 이거 해주는 이유가 좀 중요한것 같다. 이거 안해주면 내 기준 1만 증가해야하는데 있는 친구수만큼 증가해버림
            nd = temp

    # print(f"{start}의 tot ", tot)
    return tot


ans = []

for i in range(N):
    ans.append(bfs(i))
print(ans.index(min(ans)) + 1)
