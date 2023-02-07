N, M, K = map(int, input().split())

num = list(map(int, input().split()))


num.sort(reverse=True)
temp = K
rst = 0
idx = 0

# 가장 큰것만 M 번더함. K번 만큼 연속으로 더할수 있음

for _ in range(M):
    if temp == 0:
        if idx == 1:
            idx = 0
            temp = K
        else:
            idx += 1
            temp = 1
    rst += num[idx]
    temp -= 1
print(rst)
