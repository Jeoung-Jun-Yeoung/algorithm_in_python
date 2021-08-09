origin = int(input())

str = input()
arr = list(map(int,str.split()))


m = max(arr)
for i in range(0,origin):
    arr[i] = arr[i]/m*100


print(sum(arr,0.0)/len(arr))