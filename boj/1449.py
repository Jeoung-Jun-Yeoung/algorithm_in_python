import sys

input = sys.stdin.readline

N, L = map(int, input().split())

Crak = list(map(int, input().split()))

Crak.sort()

taping = N

print(Crak)

for i in range(N - 1):
    for j in range(i + 1, N):
        if (Crak[j] + 0.5) - (Crak[i] - 0.5) <= L:
            print(
                f"{Crak[i] - 0.5} ~  {Crak[j] + 0.5}, L : {L}")
            taping -= 1
print(taping)
