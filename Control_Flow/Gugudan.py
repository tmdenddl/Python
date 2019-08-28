# 구구단을 만들어보세요. while문을 사용하여 콘솔에 아래 문장들이 출력되게 프로그램을 작성하세요.
i = 1
while i < 10:
    j = 1
    while j < 10:
        print("%d * %d = %d" % (i, j, i * j))
        j += 1
    i += 1
