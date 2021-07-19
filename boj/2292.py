N = int(input())

room = 1
cnt = 6
while N > 1:
    N -= cnt
    cnt += 6
    room += 1

print(room)