N = int(input())
data = []
temp = 1
while (temp <= N):
    data.append(int(input()))
    temp = temp+1
data.sort()
data.reverse()
while True:
    if not data:
        break
    print(data.pop())
