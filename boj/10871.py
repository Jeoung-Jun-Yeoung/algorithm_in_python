n,x = map(int,input().split())

arr = list(map(int,input().split()))

for i in range(0,n):
    if(x >arr[i]):
        print(arr[i], end=' ')
