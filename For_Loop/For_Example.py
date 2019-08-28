numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 인덱스와 원소 출력
# 코드를 입력하세요.
for index in range(len(numbers)):
    print("%d %d" % (index, numbers[index]))

# 좀 더 효율적인 코딩
for index in range(len(numbers)):
    print(index, numbers[index])

# 2의 n제곱의 결과값을 출력하는 프로그램을 만드세요. 아래와 같이 2^0 = 1부터 2^10 = 1024까지 출력되어야 합니다.
NUMBER = 2
n = 10

for i in range(n+1):
    print("%d^%d = %d" % (NUMBER, i, NUMBER ** i))

# for문을 사용한 구구단:
for i in range(1, 10): # i = [1,9]
    for j in range(1,10): # j = [1,9]
        print("%d * %d = %d" % (i, j, i*j))

