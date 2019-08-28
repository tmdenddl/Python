# 빅뱅 멤버들
big_bang = ["지드래곤", "태양", "탑", "대성", "승리"]

# While문 사용시
i = 0
while i < len(big_bang):
    print(big_bang[i])
    i = i + 1

# for문 사용시
for member in big_bang:
    print(member)

# 다른 예시
for num in [1, 3, 5, 7, 9]:
    print(num * num)

# 리스트 사용시
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

# Range 사용시
for i in range(1, 11): # 1부터 10 까지
    print(i)

for i in range(10): # 0 부터 9까지
    print(i)

for i in range(3, 17, 3): # 3부터 3의 간격으로 16까지
    print(i)