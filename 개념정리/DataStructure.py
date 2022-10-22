from collections import deque
import heapq
# 배열
# 삽입/삭제 O(N)

arr = [10, 11, 12, 13]
arr[2] = 5

print(arr)

# 백터

vector = []

vector.append((123, 456))
vector.append((789, 987))

print("size:", len(vector))

for p in vector:
    print(p)

# 스택 Stack , python은 list로 사용

stack = []

stack.append(123)
stack.append(456)
stack.append(789)

print("size:", len(stack))

while len(stack) > 0:
    print(stack[-1])
    stack.pop(-1)

dq = deque()
dq.append(123)
dq.append(456)
dq.append(789)
print("size:", len(dq))

while len(dq) > 0:
    print(dq.popleft())


# 우선순위큐 파이썬은 min-heap. 루트에 가장 최소
pq = []

heapq.heappush(pq, 456)
heapq.heappush(pq, 123)
heapq.heappush(pq, 789)

print("size:", len(pq))

while len(pq) > 0:
    print(heapq.heappop(pq))


# map -> 파이썬의 딕셔너리

m = {}
m["junyeong"] = 100
m["hyenchul"] = 90
m["kungjub"] = 70

print("size:", len(m))

for k in m:
    print(k, m[k])


# 집합 SET

s = set()


print("size:", len(s))
s.add(123)
s.add(456)
s.add(456)
s.add(456)
s.add(456)
s.add(23)
s.add(32)
s.remove(32)

print(s)

# 중복이안됌, 값 삭제는 가능
