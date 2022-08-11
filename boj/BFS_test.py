from collections import deque
from collections import defaultdict
dq = deque()

s = 1

dq = deque([s])
y, x = 5, 1
dq.append(5)
n = dq.popleft()
dq = deque([[y, x]])


graph = defaultdict(list)
for i in range(5):
    n1, n2 = map(int)
    graph[n1].append(n2)
    graph[n2].append(n1)
