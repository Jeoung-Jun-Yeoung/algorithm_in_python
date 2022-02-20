
N = int(input())
data = []

for i in range(N):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[0], x[1]))

for i in data:
    print(i[0], i[1])
