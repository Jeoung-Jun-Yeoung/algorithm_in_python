import heapq

pq = []
N = int(input())

while N > 0:
    x = int(input())
    if x == 0:
        print(heapq.heappop(pq))
    else:
        heapq.heappush(pq, x)
