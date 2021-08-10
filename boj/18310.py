from sys import stdin

n = int(stdin.readline())

arr = list(map(int,stdin.readline().split()))
arr.sort()

print(arr[(len(arr) - 1) // 2])