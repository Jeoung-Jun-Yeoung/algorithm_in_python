from collections import deque

deq = deque()
rst = list()
n, k = map(int, input().split())

for i in range(1, n + 1):
    deq.append(i)
while deq:
    for _ in range(k-1):
        num = deq.popleft()
        deq.append(num)
    temp = deq.popleft()
    rst.append(temp)

print("<", end="")
for i in range(len(rst)):
    if i == len(rst) - 1:
        print(f"{rst[i]}", end="")
        break
    print(f"{rst[i]}"+", ", end="")
print(">")
