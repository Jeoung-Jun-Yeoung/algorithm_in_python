
import random
import sys
a = int(input("게임에 참가할 인원 수 :"))
if a <= 1:
    print("2인 이상 게임 참가 가능 *게임을 다시 시작하세요*")
    sys.exit()

name = []  # 유저의 이름
word = []  # 단어
for x in range(1, a+1):
    name.append(input(f"유저{x} 닉네임 :"))


print("========== GAME START ==========")

keyword = ["대나무", "무사", "사기", "기사", "사기", "무지개", "개", "기러기", "서산"]


i = 0


while len(name) != 1:
    keyword_list = random.choice(keyword)

    word.append(keyword_list)

    print(keyword_list)

    user_word = input(f"{name[i]} :")

    if user_word in word:
        print("이미 사용된 단어입니다.")
        del name[i]
        word.clear()

    elif len(user_word) == 1:
        print("2글자 이상의 단어만 사용 가능합니다.")
        del name[i]
        word.clear()

    elif keyword_list[-1] != user_word[0]:
        print("단어가 틀렸습니다.")
        del name[i]
        word.clear()

    else:
        word.append(user_word)
        i += 1
