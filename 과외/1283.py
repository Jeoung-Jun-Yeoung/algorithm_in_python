
N = int(input())

FnDic = {}


def makeShortCut(wordList):
    # enumerate() -> index와 값을 반환해주는 함수
    for idx, word in enumerate(wordList):
        if word[0] not in FnDic:
            FnDic[word[0].upper()] = True
            FnDic[word[0].lower()] = True
            wordList[idx] = '[' + word[0]+']'+word[1:]
            return
        # 만약 첫 단어에서 못 걸렀다면? -> 이때는 순서대로 보면 된다.
    for idx, word in enumerate(wordList):
        for idx2, char in enumerate(word):
            if char not in FnDic:
                FnDic[char.upper()] = True
                FnDic[char.lower()] = True
                wordList[idx] = word[:idx2] + '[' + char + ']' + word[idx2+1:]
                return


for i in range(N):
    s = input().split()
    makeShortCut(s)
    print(*s)

# 처음부터 쭉 보면서 dic에 없다면 추가해주면 됨.
# print(f"rst {RstList}")

# 등록했으면 등록한 ch에 괄호를 씌워야 함.
