from sys import stdin

h,w = map(int,stdin.readline().split())

arr = [-1 for _ in range(h)]
rst_arr = [list() for _ in range(h)]

for i in range(h):
    arr[i] = list(map(str,stdin.readline().split()))
    temp = arr[i][0]
    count = -1
    for j in temp:
        if count != -1:
            count += 1
        if j == 'c':
            count = 0
        rst_arr[i].append(count)
            
for i in range(h):
    for j in range(w):
        print(rst_arr[i][j],end=' ')
    print()
        