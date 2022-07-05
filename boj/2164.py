from collections import deque

q = deque()
N = int(input())
for i in range(N):
    q.append(i + 1)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.popleft())
