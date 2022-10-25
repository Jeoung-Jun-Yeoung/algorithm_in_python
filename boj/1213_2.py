text = input()
d = dict()

for ch in text:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

if sum(i % 2 for i in d.values()) > 1:
    print("I'm Sorry Hansoo")
else:
    # ans = half를 만들어서 넣어준다.
    half = ""
    for k, v in sorted(d.items()):
        half += k * (v // 2)
        # 개수에 절반을 저장..

    ans = half

    for k, v in d.items():
        if v % 2 != 0:
            ans += k
            break
    ans += "".join(reversed(half))
    print(ans)
