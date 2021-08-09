<<<<<<< HEAD
origin = int(input())

str = input()
arr = list(map(int,str.split()))


m = max(arr)
for i in range(0,origin):
    arr[i] = arr[i]/m*100


print(sum(arr,0.0)/len(arr))
=======
from sys import stdin

k,n = map(int,stdin.readline().split())

array = []
for i in range(k):
    array.append(int(stdin.readline()))

max_lan = max(array)
start = 1
end = max_lan
temp = 0

while start <= end:
    rst = 0
    mid = (start + end)//2
    for i in array:
        rst += i//mid
    if rst >= n:
        start = mid + 1
        temp = mid
    else:
        end = mid - 1
print(temp)
>>>>>>> 854d221704ef3d06198768803f6e5113abf0d921
