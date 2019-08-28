# vocabulary.txt의 첫 줄부터, 콘솔에 한국어 뜻을 알려주면 학생이 영어 단어를 입력하는 방식입니다.
# 맞는 답이 나오면 맞았습니다!가 출력되고 틀린 답이 나오면 아쉽습니다. 정답은 OOO입니다. 형식으로 나옵니다.

# 파일 읽기
read_file = open('vacabulary.txt', 'r')

for line in read_file:
    # 영어 단어와 한국어 뜻을 공백 없이 분리
    data = line.strip().split(": ")
    english_word = data[0]
    korean_word = data[1]

    # 영어 단어 제시 후 문제 제시
    guess = input("%s: " % korean_word)
    if guess == english_word:
        print("정답입니다.\n")
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" % english_word)

# 파일 닫기
read_file.close()
