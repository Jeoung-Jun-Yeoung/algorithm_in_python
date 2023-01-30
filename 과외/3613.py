value = input()

transValue = ''

if '_' in value:
    # c++ _가 있으면 c++후보 가장 확실함.
    # 이때 만약 isupper() == True이면
    flag = False
    ck = 0
    for ch in value:
        # print(f"ch {ch} flag {flag} transValue {transValue}")
        if ch.isupper():
            print('Error!')
            upper = True
            break
        if ch == '_':
            ck += 1
            flag = True
            continue
        if flag == True:
            transValue += ch.upper()
            flag = False
            continue
        transValue += ch
    if len(value) == ck:
        print('Error!')
    if not upper:
        print(transValue)

else:
    if value.islower():
        # 만약 _가 없고 모든 문자열이 소문자면 그대로 출력하면 됌.
        print(value)
    else:
        ck = 0
        # 전부다 대문자인 경우에는 c++도 아니고 java도 아님. 체크해야함
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
