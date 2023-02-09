import collections
# 예제
# 5457
# 3
# 6 7 8
# print(help(set))
wantCh = int(input())

# 예외처리를 할때 범위에서 주어진 최대,최소값을 넣어봄

errBtnNum = int(input())

if errBtnNum != 0:
    errBtn = list(map(int, input().split()))
else:
    errBtn = []

remoCon = set()

nowCh = 100

for i in range(0, 10, 1):
    if i not in errBtn:
        remoCon.add(i)

if wantCh == nowCh:
    print(0)
    exit()
# 같은 경우 예외처리

# 가능한 모든 채널을 만든다.
# 500,000 -> 5,000,000
# 0 ~ 5,000,000
# 맨 처음 채널을 정하고 다 해보는데,
# 맨 처음 채널이 될 수 있는 후보가 5백만개


minPs = abs(wantCh - nowCh)
for candiCh in range(5000001):
    # candiCh와 remoCon을 비교
    # if candiCh > minPs + wantCh:
    #     break
    #
    isCh = True
    cnt = 0
    tempCandiCh = str(candiCh)
    # candiCh에 모든 버튼을 리모콘으로 누를 수 있는지
    # print(f'tempCandiCh {tempCandiCh} ')
    # print(remoCon)
    for tC in tempCandiCh:
        if int(tC) in remoCon:
            # print(f'tc {tC} 누를수 있다.')
            # 누를수 있음
            cnt += 1
        else:
            # print(f'tc {tC} 누를수 없다.')
            # 누를 수 있는데 누를수없다고 나온다.
            isCh = False
            break
    if isCh:
        # 만든게 맞으면 cnt로 답을 처리함?
        ps = cnt
        ps += abs(candiCh - wantCh)
        minPs = min(minPs, ps)

print(minPs)

# 누르는 작업.
# cnt 만큼 눌러야 하고
# candiCh - wantCh 만큼 눌러야 함
