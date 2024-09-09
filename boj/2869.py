A, B, V = map(int, input().split())

now = 0

day = 0

now = V // A
print(now)
temp = ((V % A) * B) // A
print(temp)
