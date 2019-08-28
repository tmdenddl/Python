# 이번에는 randint 함수와 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 테스트하는 프로그램을 써보세요.

from random import randint

# 파일 읽기
read_file = open('vacabulary.txt', 'r')

vocab = {}

for line in read_file:
    # 영어 단어와 한국어 뜻을 공백 없이 분리
    data = line.strip().split(": ")
    english_word = data[0]
    korean_word = data[1]

    # 영어 단어와 한국어 뜻을 사전에 저장
    vocab[korean_word] = english_word


# 사전 내용물 확인 코드
print(vocab)

# Key에 대한 리스트 만들기
keys = list(vocab.keys())

# 단어 수 카운트
no_of_words = len(keys)

# 무한루프 실행
while True:
    # randint를 사용하여 랜덤한 숫자 만들기
    word_no = randint(0, no_of_words - 1)

    # 영어 단어와 한국어 뜻
    english = vocab[word_no]
    korean = vocab[english]

    # 영어 단어 문제 제시
    guess = input("%s: " % korean)

    if guess == "q":
        break
    elif guess == english:
        print("정답입니다")
    else:
        print("아쉽습니다. 정답은 %s입니다." % english)


# 파일 닫기
read_file.close()
