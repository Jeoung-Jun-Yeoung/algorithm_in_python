arr = list()
for i in range(0,10):
    arr.append(int(input())%42)

if len(arr) == len(set(arr)):
    print(len(arr))
else:
    print(len(set(arr)))