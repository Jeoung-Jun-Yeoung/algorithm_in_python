N = int(input())

member = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    member.append(list([age, name, i]))

member.sort(key=lambda x: (x[0], x[2]))


for i in range(N):
    print(member[i][0], member[i][1])
