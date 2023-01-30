value = input()

transValue = ''

if '_' in value:
    # c++ 후보
    # 근데 대문자가 있으면 이상한 케이스

    if value.isupper():
        print('is upper Error!')
    else:
        # _와 소문자의 조합
        # 여기서 이상한 경우가 뭐가 있을까?

        # _와 소문자의 조합인데, 만약에 _로 끝나는 경우에는 c++의 올바른 변수명이 아님
        if value[len(value) - 1] == '_':
            print('Error!')
        # _로 시작해도 에러임
        if value[0] == '_':
            print('Error!')
        else:
            # 여기까지 오면 _로 시작하는것도 아니고 _로 끝나지도 않음. _와 소문자의 조합인데 알파벳 소문자로 시작
            flag = False
            ck = 0
            for ch in value:
                if ch == '_':
                    if flag == True:
                        # _가 연속으로 나와도 에러
                        print('Error!')
                    ck += 1
                    flag = True
                    continue
                if flag == True:
                    transValue += ch.upper()
                    flag = False
                    continue
                transValue += ch
            # 만약 _로만 이뤄졌다면? 에러임
            if len(value) == ck:
                print('Error!')
            else:
                print(transValue)
else:
    flag = False
    ck = 0
    # 일단 _가 없으면 넘어옴
    # 대문자가 있으면 에러임
    if value.islower():
        print('Error!')
    for ch in value:
        if ch.isupper():
            transValue += '_'
            transValue += ch.lower()
            ck += 1
        else:
            transValue += ch
    if len(value) == ck:
        print('Error!')
    else:
        print(transValue)

        # if '_' in value:
        #     # c++ _가 있으면 c++후보 가장 확실함.
        #     # 이때 만약 isupper() == True이면
        #     flag = False
        #     ck = 0
        #     for ch in value:
        #         # print(f"ch {ch} flag {flag} transValue {transValue}")
        #         if ch.isupper():
        #             print('Error!')
        #             upper = True
        #             break
        #         if ch == '_':
        #             ck += 1
        #             flag = True
        #             continue
        #         if flag == True:
        #             transValue += ch.upper()
        #             flag = False
        #             continue
        #         transValue += ch
        #     if len(value) == ck:
        #         print('Error!')
        #     if not upper:
        #         print(transValue)

        # else:
        #     if value.islower():
        #         # 만약 _가 없고 모든 문자열이 소문자면 그대로 출력하면 됌.
        #         print(value)
        #     else:
        #         ck = 0
        #         # 전부다 대문자인 경우에는 c++도 아니고 java도 아님. 체크해야함
        #         for ch in value:
        #             if ch.isupper():
        #                 transValue += '_'
        #                 transValue += ch.lower()
        #                 ck += 1
        #             else:
        #                 transValue += ch
        #         if len(value) == ck:
        #             print('Error!')
        #         else:
        #             print(transValue)
