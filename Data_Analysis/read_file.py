# open 함수를 써서 chicken.txt파일을 엽니다. 'r'은 Read의 약자입니다.
in_file = open('chicken.txt', 'r')

# 라인 사이에 빈 공간이 있음
for line in in_file:
    print(line)

# 라인 사이에 빈 공간이 없음
for line in in_file:
    print(line.strip())

# 한번 연 파일은 닫아줘야지 메모리 낭비가 안 된다
in_file.close()