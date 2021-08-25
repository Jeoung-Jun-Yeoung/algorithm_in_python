from sys import stdin
from collections import deque, defaultdict

n = int(stdin.readline())
graph = defaultdict(list)
n1,n2 = map(int,stdin.readline().split())
visted = [False] * (n + 1)
cnt = int(stdin.readline())

depth = 0

for i in range(cnt):
    temp_n1, temp_n2 = map(int,stdin.readline().split())
    graph[temp_n1].append(temp_n2)
    graph[temp_n2].append(temp_n1)

dq = deque([[n1,depth]])

# dequq를 선언할때는 원하는 자료형 자체를 표햔해야한다.
# popleft()가 안된 이유는 [node,depth]를 pop했을때 [여기에서 왼쪽, 즉 node만 튀어나왔기때문이다.]

flag = 0
while dq:
    node,depth = dq.popleft()
    visted[node] = True
    if node == n2:
        print(depth)
        flag = 1
        break
    for i in graph[node]:
        if visted[i] == True:
            continue
        dq.append([i,depth+1])
    # dq.append([i, depth+1 for i in graph[node] if visted[i] != True])
if flag == 0:
    print(-1)