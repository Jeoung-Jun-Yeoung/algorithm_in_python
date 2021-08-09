from sys import stdin

h,w = map(int,stdin.readline().split())

arr = [0 for _ in range(h)]

for i in range(h):
    arr[i] = list(map(str,stdin.readline().split()))

for i in range(h):
    for j in range(w):
        if arr[i][j] == "c":
            print('c')
        else:
            print('dot')