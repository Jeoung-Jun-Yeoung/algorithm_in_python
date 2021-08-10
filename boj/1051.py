from sys import stdin

col,row = map(int,stdin.readline().split())

arr = [0 for _ in range(col)]
for i in range(col):
    arr[i] = list(map(int,stdin.readline().split()))
print(arr)