N, K = map(int, input().split())

x = 1
y = 1
z = 1

for n in range(1, N + 1):
    x = x * n

for k in range(1, K + 1):
    y = y * k

Z = N - K
for temp in range(1, Z + 1):
    z = temp * z

y = z * y

print(int(x/y))
