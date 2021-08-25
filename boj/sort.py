arr = [1, 5,4, 3, 10]

arr = sorted(arr)

arr = sorted(arr, reverse=True)

arr = [[1, 2, 3, 4,5], [2, 1, 4,5,5], [3,3,3,3,3],[1,1,1,1,1]]
arr = sorted(arr, key=lambda x : x[3])
print(arr)
arr = sorted(arr, key=lambda x: x[0], reverse=True)
print(arr)