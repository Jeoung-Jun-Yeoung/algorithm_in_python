import sys

input = sys.stdin.readline

cache = [-1] * 91
cache[0] = 0
cache[1] = 1
N = int(input())

for i in range(2, N+1):
    # 바텀업방식은 순서가 중요하다. 어떤 부분문제의 답을 알아야 그 다음을 구할부분문제의 답을 구할수 있나?
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[N])
