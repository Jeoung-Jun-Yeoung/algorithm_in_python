# 공포도가 x인 사람은 인원이 x명인 그룹에 속해야함


N = int(input())
people = list(map(int, input().split()))

people.sort(reverse=True)

print(people)

goAway = []
count = 0
while True:
    val = people.pop()
    goAway.append(val)
    print(f'goAway {goAway}')
    if len(goAway) == val:
        count += 1
        goAway.clear()
    if len(people) == 0:
        break
print(count)
