from functools import cache
import sys

input = sys.stdin.readline
MOD = 1000000000
N = int(input())

# 문제점
# 1. DP문제 인데 규칙을 찾으려고 함. 점화식을 세워야 하는데 간단한 규칙 파악으로 문제의 답을 해결 할 수 있다고 생각.
# 2. 첫번째에 주목함. 9로 시작, 8로 시작. 그런데 보통 DP문제는 앞이 중요한게 아니라 마지막에 어떻게 끝나는지에
# 따라서 점화식을 보통 세움.

# f(n,d) = 길이가 n이고 마지막 숫자가 d인 계단수의 개수
# f(n,0) + f(n,1) + f(n,2) . . . . f(n,9) % MOD -> 답

# f(n,d) = f(n - 1, d - 1) + f(n - 1 , d + 1)
#          if d > 0             if d < 9
# 초기값 f(1,1~9) = 1

# cache[n][d] = 길이가 n, 마지막 숫자가 d인 계단수 개수
cache = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    cache[1][i] = 1

for i in range(2, 101):
    # 1일때는 채웠으니까 길이가 2부터 보면 됨
    for j in range(10):
        if j > 0:
            cache[i][j] += cache[i - 1][j - 1]
            # 0 보다 클때는 -1 한걸 더해줌
        if j < 9:
            # 9보다 작을때는 +1한걸 더해줌
            # 이렇게 하면 9는 첫번째 if문만 걸리고, 0은 두번째 if문만 걸림. 나머지는 둘다걸려서 만족.
            cache[i][j] += cache[i - 1][j + 1]

ans = 0

for i in range(10):
    ans += cache[N][i]
    # 다른 언어에서는 오버플로우 방지로 더할때마다 MOD로 나머지를 취해야 함.
print(ans % MOD)
