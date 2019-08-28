# 이번에는 randint 함수와 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 테스트하는 프로그램을 써보세요.

from random import randint

# 파일 읽기
read_file = open('vacabulary.txt', 'r')

english_words = []
korean_words = []
no_of_words = 0

for line in read_file:
    # 영어 단어와 한국어 뜻을 공백 없이 분리
    data = line.strip().split(": ")

    # 영어 단어 리스트에 입력
    english_word = data[0]
    english_words.append(english_word)

    # 한국어 뜻 리스트에 입력
    korean_word = data[1]
    korean_words.append(korean_word)

    # 단어 수 카운트
    no_of_words += 1

# 제대로 나뉘었는지 확인 코드
print(english_words)
print(korean_words)

# 무한루프 실행
i = 1
while i > 0:
    # randint를 사용하여 랜덤한 숫자 만들기
    word_no = randint(0, no_of_words - 1)

    # 영어 단어 문제 제시
    guess = input("%s: " % korean_words[word_no])

    if guess == "q":
        break
    elif guess == english_words[word_no]:
        print("정답입니다")
    elif guess != english_words[word_no]:
        print("아쉽습니다. 정답은 %s입니다." % english_words[word_no])


# 파일 닫기
read_file.close()
