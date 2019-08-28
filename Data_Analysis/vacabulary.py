# 이 프로그램은 콘솔로 영어 단어와 한국어 뜻을 받고, vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리합니다.
# 프로그램을 실행하면 영어 단어와 한국어 뜻을 입력할 수 있습니다. 단어-뜻을 입력할 때마다 vocabulary.txt에 단어가 정리됩니다.
# 프로그램을 끝내려면, 알파벳 q를 입력하면 됩니다.

# 파일 열기 및 쓰기
write_file = open('vacabulary.txt', 'w')

while True:
    # 영어 단어 입력
    english = input("영어 단어를 입력하세요: ")
    if english == "q":  # q입력시 종료
        break

    # 한국어 뜻 입력
    korean = input("한국어 뜻을 입력하세요: ")
    if korean == "q":  # q입력시 종료
        break

    # 파일에 쓰기
    write_file.write("%s: %s\n" % (english, korean))

# 파일 닫기
write_file.close()