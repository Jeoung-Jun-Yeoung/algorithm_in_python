def solution(s):
    answer = []
    # 구현문제

    # x의 모든 0을 제거한다

    # 1-> s를 리스트로 바꾸고, 0 개수를 세고, 0 개수만큼 remove()한다. 이때 제거 개수를 센다.

    # 2-> 이후 리스트를 다시 문자열로 변환한다.

    # x의 길이를 c라고 하면 x를 c를 2진법으로 표현한 문자열로 바꾼다.

    # 3-> 그렇게 나온 x의 길이를 2진법으로 바꾼다.

    # 1 ~ 3을 반복하고 과정 체크. 언제까지? x == "1"일때까지

    # 이과정에서 몇번의 2진변환을 했는지, 그리고 제거된 0의 개수를 체크한다.

    # s가 1이 될때까지 반복한다.
    cnt = 0
    zero = 0
    while True:
        x = list(s)

        print("x ", x)

        cnt += 1
        cntZero = x.count("0")

        if x.count("0") != 0:
            zero += x.count("0")
        # 0의 개수세기
            for _ in range(x.count("0")):
                x.remove("0")

        s = "".join(x)

        temp_x = []

        toChange = len(s)

        while toChange > 0:
            if toChange % 2 != 0:
                temp_x.append("1")
            else:
                temp_x.append("0")
            toChange = toChange // 2

        temp_x.reverse()
        print("이진변환결과 ", temp_x)
        isX = "".join(temp_x)
        print("문자열변환결과 ", isX)

        if cnt == 3:
            break
        if isX == "1":
            break

        s = isX
        print("next X = ", x)
    print(f"count {cnt} zero {zero}")

    return answer


solution("110010101001")
