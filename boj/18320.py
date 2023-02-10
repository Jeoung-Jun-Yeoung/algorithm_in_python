n = int(input())

home = list(map(int, input().split()))
home.sort()
print(home[(n-1) // 2])

# nowDis = 300000
# temp = 0
# minDis = []
# for i in range(4):
#     distance = 0
#     for j in range(4):
#         distance += abs(home[i] - home[j])
#     minDis.append(distance)

# val = min(minDis)
# print(home[minDis.index(val)])

# print(index.find(min(index)))
