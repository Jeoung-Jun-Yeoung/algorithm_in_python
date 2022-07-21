import heapq

pq = []
N = int(input())

while N > 0:
    x = int(input())
    if x == 0:
        if len(pq) == 0:
            print(0)
        else:
            print(heapq.heappop(pq))
    else:
        heapq.heappush(pq, x)
    N = N - 1
