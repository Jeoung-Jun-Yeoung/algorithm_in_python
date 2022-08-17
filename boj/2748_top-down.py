import sys

input = sys.stdin.readline

cache = [-1] * 91
cache[0] = 0
cache[1] = 1

cnt = 0


def f(n):
    global cnt
    cnt += 1
    if cache[n] == -1:
        # 처음으로 구하는것

        cache[n] = f(n-1) + f(n-2)
    return cache[n]


print(f(int(input())))
print(cnt)
