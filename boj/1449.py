import sys
input = sys.stdin.readline
N, L = map(int, input().split())
coord = [False] * 1001
# 구멍이 난 좌표만 True로 바꿔준다.
for i in map(int, input().split()):
    coord[i] = True
# 점프해야하기때문에 for문을 쓰는것 보다 점프할 인덱스 변수를 만들어 주는 것이 좋다.

x = 0
ans = 0
while x < 1001:
    if coord[x]:
        ans += 1
        x += L
    else:
        x += 1

print(ans)

# import sys
# input = sys.stdin.readline
# N, L = map(int, input().split())
# Crak = list(map(int, input().split()))
# -> 좌표 압축.
# Crak.sort()
# taping = N
# print(Crak)
# for i in range(N - 1):
#     for j in range(i + 1, N):
#         if (Crak[j] + 0.5) - (Crak[i] - 0.5) <= L:
#             print(
#                 f"{Crak[i] - 0.5} ~  {Crak[j] + 0.5}, L : {L}")
#             taping -= 1
# print(taping)
