

def Java2CPP(value: str) -> str:
    if '_' in value:
        return None
    transValue = ''
    if value[0].isupper():
        return None

    for ch in value:
        if ch.isupper():
            transValue += '_'
            transValue += ch.lower()
        else:
            transValue += ch
    return transValue


def CPP2Java_v2(value: str):
    pass


def CPP2Java(value: str) -> str:
    for c in value:
        if c.isupper():
            return None
    # if any([c.isupper() for c in value]):
    #       return None

        # _와 소문자의 조합인데, 만약에 _로 시작하거나, 끝나는 경우에는 c++의 올바른 변수명이 아님
        if value[-1] == '_' or value[0] == '_':
            return None

        # 앞글자와 뒷글자가 영소문자가 보장됨
        transValue = ''
        # 여기까지 오면 _로 시작하는것도 아니고 _로 끝나지도 않음. _와 소문자의 조합인데 알파벳 소문자로 시작
        flag = False
        for ch in value:
            if ch == '_':
                if flag:
                    return None
                flag = True
            elif flag:
                transValue += ch.upper()
                flag = False
            else:
                transValue += ch

    return transValue


value = input()


cppName, java_name = Java2CPP(value), CPP2Java(value)

if cppName is not None:
    print(cppName)
elif java_name is not None:
    print(java_name)
else:
    print('Error!')
