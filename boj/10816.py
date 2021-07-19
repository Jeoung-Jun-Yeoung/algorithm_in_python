from sys import stdin
N = int(stdin.readline())
arr1 = list(map(int,stdin.readline().split())) 
# arr1 을 통해 카운트를 하면서 value로 cnt한 값을 넣어준다.
# defaultdict 둘다 구현하기.
M = int(stdin.readline())
arr2 = list(map(int,stdin.readline().split()))

for i in range(M):
    print(arr1.count(arr2[i]),end=' ')