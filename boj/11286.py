import heapq
import sys

input = sys.stdin.readline

pq = []
N = int(input())

while N > 0:
    x = int(input())
    if x == 0:
        if len(pq) == 0:
            print(0)
        else:
            print(heapq.heappop(pq)[1])
            # heaqp.heappop(pq) if heappop else 0 -> 위 조건문 두개랑 같은 의미
    else:
        heapq.heappush(pq, (abs(x), x))

    N = N - 1
