import sys

input = sys.stdin.readline

N = int(input())
req = list(map(int, input().split()))
M = int(input())

low = 0
high = max(req)
mid = (low + high) // 2
# 가운데니까 절반.
ans = 0


def is_possible(mid):
    # 각 지방마다 얼마를 줄지?
    # 총 합 M과 비교해서 초과여부 판단
    # for r in req:
    # 위 for문을 돌면서 total변수를 만들고 합해도된다.
    return sum(min(r, mid) for r in req) <= M
    # 둘중 작은값을 주면 된다.
    # r이 작으면 미드보다 r이 작은거는 그냥 r을 주면됨.
    # mid가 작으면 줄수 있는 한계가 mid이기게 mid를 줘야함


while low <= high:
    # low는 항상 high보다 작음
    # print(f"low : {low} mid : {mid} high : {high} ans : {ans}")
    if is_possible(mid):
        # 국가 총 예산으로 감당이 가능한지? 해당 mid로 상한선을 설정했을떄 감당가능?
        low = mid + 1
        # 가능한 경우에는 상한선을 늘려봐도 된다. low를 늘리면됨.
        # mid도 가능하니까 포함안함
        ans = mid
        # 가능하니까 정답도 mid로 일단 설정
    else:
        high = mid - 1
        # 상한선을 옴긴다.
    mid = (low + high) // 2
    # low or high도 바뀌니까 미드도 갱신한다.
print(ans)
