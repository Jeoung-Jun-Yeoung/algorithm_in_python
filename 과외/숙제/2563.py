n = int(input())

# think 종이는 여러장 일 수 있다.
# 전체 종이가 안곂쳤다면 n * 100이 색종이의 크기.
# 이때 곂치는 부분만 n * 100에서 빼준다
# n * 100 - 곂치는 부분의 길이
# papaer 길이 확인


# 100 * 100 도화지를 그리고, 채운다. 이후 채운 개수를 센다.
paper = [[0] * 100 for i in range(100)]

for i in range(n):
    x, y = map(int, input().split())

    for i in range(x, x+10, 1):
        for j in range(y, y+10, 1):
            if paper[i][j] == 0:
                paper[i][j] = 1
ck = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            ck += 1

print(ck)
