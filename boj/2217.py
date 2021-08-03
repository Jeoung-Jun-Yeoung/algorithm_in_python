from sys import stdin

n = int(stdin.readline())
arr = []
w = []

for i in range(n):
    rope = int(stdin.readline())
    arr.append(rope)
arr.sort(reverse=True)
ck = 1
if n == 1:
    print(rope)
else:    
    for i in range(n):
        w.append(arr[i]*ck)
        ck += 1
    print(max(w))
