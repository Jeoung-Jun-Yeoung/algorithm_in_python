def solution(s):
    answer = 0

    # cur -> 현재 알파벳. 제일 앞부터 자르니까 0번인덱스 알파벳을 cur로 잡고 시작
    # comStr -> 0번째를 잘라낸 문자열
    def countLen(u):
        # -> 너무 잘라서 문제가 생긴것 같습니다.
        # 2단위로 잘라서야하는데
        comStr = s
        cur = s[:u]
        rstStr = ''
        cnt = 1
        compareChar = ''

        for index in range(u, len(comStr), u):
            compareChar = comStr[index: index + u]
            # print(f'cur {cur} compareChar {compareChar} cnt {cnt} rstStr {rstStr}')
            # aabbaccc
            # s[3:7]
            if cur == compareChar:
                # 1 : abbaccc,
                cnt += 1
            else:
                # 2 : bbaccc
                if cnt == 1:
                    rstStr += cur
                else:
                    rstStr += str(cnt) + cur
                cur = compareChar
                cnt = 1

        if cnt == 1:
            rstStr += cur
        else:
            rstStr += str(cnt) + cur
        # print(f'rstStr {rstStr}')
        return(len(rstStr))
    # 마지막 인덱스 처리

    rst = []
    for i in range(1, len(s) + 1):
        rst.append(countLen(i))
    # print(rst)
    # print(min(rst))
    return min(rst)

# ab ab cd cd  ab ab cd cd

# aabbaccc -> 7 --> 1개단위: 2a2ba3c
