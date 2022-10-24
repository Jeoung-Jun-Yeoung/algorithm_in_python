import heapq as hq
import sys

input = sys.stdin.readlind

pq = []

for _ in range(int(input())):
    x = int(input())

    if x == 0:
        hq.heappush(pq, (abs(x), x))

    else:
        if pq:
            hq.heappop(pq[0])
        else:
            print(0)
