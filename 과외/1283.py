# 문제
# 한글 프로그램의 메뉴에는 총 N개의 옵션이 있다.
# 각 옵션들은 한 개 또는 여러 개의 단어로 옵션의 기능을 설명하여 놓았다.
# 그리고 우리는 위에서부터 차례대로 각 옵션에 단축키를 의미하는 대표 알파벳을 지정하기로 하였다. 단축키를 지정하는 법은 아래의 순서를 따른다.

# 먼저 하나의 옵션에 대해 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다. 만약 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정한다.
# 만약 모든 단어의 첫 글자가 이미 지정이 되어있다면 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정한다.
# 어떠한 것도 단축키로 지정할 수 없다면 그냥 놔두며 대소문자를 구분치 않는다.
# 위의 규칙을 첫 번째 옵션부터 N번째 옵션까지 차례대로 적용한다.

# 입력
# 첫째 줄에 옵션의 개수 N(1 ≤ N ≤ 30)이 주어진다.
# 둘째 줄부터 N+1번째 줄까지 각 줄에 옵션을 나타내는 문자열이 입력되는데 하나의 옵션은 5개 이하의 단어로 표현되며,
# 각 단어 역시 10개 이하의 알파벳으로 표현된다. 단어는 공백 한 칸으로 구분되어져 있다.

N = int(input())

FnDic = {}
RstList = []
for i in range(N):
    # 1. 먼저 왼쪽에서 오른쪽 순서로 단어의 첫 글자가 단축키로 지정되어있는지 확인
    # 이때 1번이 안되면 다음 단어 첫글자를 지정.
    # 모든 단어의 첫글자가 안되면 첫 단어로 돌아와 그 다음 알파벳을 지정
    # 모든게 지정되면 그냥 둔다.
    AllWordList = list(input().split())

    # print(f"All {AllWordList}")

    # 모든 단어의 첫글자만 보면 된다. 첫글자가 등록되어 있지 않다면 등록하고 다음꺼 봄
    # 만약 첫글자가 등록되어 있다면? 다음 단어의 첫 글자를 본다. 이렇게 모든 단어의 첫 글자를 봤으면 그담부터는 차례대로 보면서 등록한다.
    flag = False
    RstWord = ''

    for Word in AllWordList:

        if Word[0] not in FnDic:
            # 단어의 첫 글자가 등록되어 있지 않은 경우.
            # 등록을 시킨다.
            # 등록시킨 경우 AllWordList에 남아있는거까지 전부 쓸어담아야함. 매우중요한 힌틍니듯!@!!
            FnDic[Word[0].upper()] = True
            FnDic[Word[0].lower()] = True
            # 이후에는 괄호를 씌우고 빠져 나가면 됨.

            RstWord += ' ['+Word[0]+']'
            for i in range(1, len(Word)):
                RstWord += Word[i]
            flag = True
        else:
            RstWord += " "+Word
            # RstWord에 값을 담음 [N]ew는 만든 상황.

    if flag:
        # New [f]ile
        # 이 조건에서 걸린다. Font는 위 조건에서 못거른 단어인데 일단 RstWord에 넣어줬으니 여기서 어팬드가 되고 나중에 원본이 변환됨 ㅠ
        RstList.append(RstWord)
    if not flag:
        # 만약 첫 단어에서 못 걸렀다면? -> 이때는 순서대로 보면 된다.

        result = ' '.join(s for s in AllWordList)
        rst = list(result)
        for i in range(len(rst)):
            if rst[i] not in FnDic:
                FnDic[rst[i].upper()] = True
                FnDic[rst[i].lower()] = True
                rst.insert(i, '[')
                # print(f"rst after {rst}")
                rst.insert(i + 2, ']')
                # print(f"rst is {rst}")
                break
        result = "".join(s for s in rst)
        RstList.append(result)

for s in RstList:
    if s[0] == ' ':
        s = s[1:]
    print(s)
# 처음부터 쭉 보면서 dic에 없다면 추가해주면 됨.
# print(f"rst {RstList}")

# 등록했으면 등록한 ch에 괄호를 씌워야 함.
