def solution(id_list, report, k):
    answer = []

    new_list = []
    for de in report:
        if de not in new_list:
            new_list.append(de)

    # 중복제거
    d = dict()

    # 내가 누굴 신고했는지 체크. 이때

    for re in new_list:
        name1, name2 = re.split()
        if name2 in d:
            d[name2] += 1
        else:
            d[name2] = 1
    # 신고횟수 저장

    print(f"d {d} ")
    for i_d in id_list:
        target = 0
        for tmp in new_list:
            name1, name2 = tmp.split()
            if name1 == i_d:
                print(f"id {i_d} name1 {name1} name2 {name2}")
                if d[name2] >= 2:
                    target += 1
        answer.append(target)
    print(answer)

    # 누가 몇번 신고 당했는지 알게 됨.

    return answer
