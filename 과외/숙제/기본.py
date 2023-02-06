a = [2] * 3
print(a)  # [2,2,2]

a[2] = 5
print(a)  # [2,2,5]

a = [[2] * 3] * 2
print(a)  # [[2,2,2,],[2,2,2]]

a[0][0] = 1
print(a)

b = [2] * 3
a = [b] * 2
a[0][0] = 1  # b[0] = 1

a = [[2] * 3 for i in range(2)]

M = N = 5
a = [[] for i in range(N)]
# 빈 리스트 만들기
a[0].append(1)
print(a)  # [[1],[],[],[],[]]

a = [[None] * i for i in range(N)]

# N행 M열을 만들때
a = [[False] * M for i in range(N)]
