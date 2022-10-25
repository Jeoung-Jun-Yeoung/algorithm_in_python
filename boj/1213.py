text = input()

tes = list(text)
tes.sort()


# 알파벳 개수세기

alph = ["A", "B", "C", "D", "E", "F",
        "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X",
        "Y", "Z"]

cnt = []

odd = True
is_odd = 0

for ck in alph:
    cnt.append(tes.count(ck))
    if tes.count(ck) % 2 != 0:
        is_odd += 1
    if is_odd >= 2:
        odd = False

# odd 가 트루라는건 홀수가 2개 이상은 없다는 이야기
answer = ""
ans = []
if odd:
    # 홀수가 최소 1개 이하를 보장

    # 홀수가 한개인 상황
    # let = max(cnt)
    # temp = cnt.index(let)
    # # temp 에는 젤 많이 쓰인 알파벳 인덱스가 담긴다.

    # for _ in range(let):
    #     ans.append(alph[temp])
    # print("ans ", ans)
    # cnt.pop(temp)
    # cnt.insert(temp, 0)

    # 해당 인덱스에 0을 넣어줌.
    mem = -1

    while sum(cnt) > 0:
        let = max(cnt)
        temp = cnt.index(let)
        flag = False
        if let % 2 != 0:
            # 홀수인상황
            mem = temp
            if mem == 1:
                cnt.pop(temp)
                cnt.insert(temp, 0)
                continue
            else:
                flag = True
                # 1인경우 밑에꺼 하면 안됌.
                # 해당 인덱스를 기억해둔다.
        # temp 에는 젤 많이 쓰인 알파벳 인덱스가 담긴다.
        if flag:
            for _ in range(let - 1):
                ans.insert(len(ans) // 2, alph[temp])
        else:
            for _ in range(let):
                ans.insert(len(ans) // 2, alph[temp])
        cnt.pop(temp)
        cnt.insert(temp, 0)
    if mem != -1:
        ans.insert(len(ans) // 2, alph[mem])

    for ch in ans:
        answer += ch
    print(answer)
else:
    print("I'm Sorry Hansoo")
