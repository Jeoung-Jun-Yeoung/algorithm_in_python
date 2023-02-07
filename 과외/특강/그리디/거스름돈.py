# 500, 100, 50, 10

# 거슬러 줘야 할 동전의 최소 개수.거슬러줄돈은 항상 N

N = int(input())

coin = [500, 100, 50, 10]

remoney = 0
for c in coin:
    remoney += N // c
    N = N % c
