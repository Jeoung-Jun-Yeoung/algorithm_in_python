from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

N = int(input())
HaveCard = list(map(int, input().split()))
HaveCard.sort()
M = int(input())
isHave = list(map(int, input().split()))

result = []

for temp in isHave:
    if 0 == bisect_right(HaveCard, temp) - bisect_left(HaveCard, temp):
        result.append(0)
    else:
        result.append(1)

# print(f"N : {N} M : {M} HaveCard {HaveCard} isHave {isHave}")

# print(' '.join(map(str,ans)))
# print(*ans)
# 둘다 정답 출력

for r in result:
    print(r, end=" ")
