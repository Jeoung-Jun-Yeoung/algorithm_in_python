from sys import stdin

n = int(stdin.readline())

arr = list(map(int,stdin.readline().split()))
arr.sort()

if len(arr)%2 == 0:
    print(arr[len(arr)//2 - 1])
    
elif len(arr)%2 != 0:
    print(arr[round(len(arr)//2) - 1])