# 리스트 정의
numbers = [1, 2, 3, 4, 5, 6]
names = ["윤수", "혜린", "태호", "영훈"]

# 리스트 출력하기
print(numbers) # numbers라는 리스트를 출력하니 [1, 2, 3, 4, 5, 6]이 나왔습니다.
print(names) # names라는 리스트를 출력하니 ['윤수', '혜린', '태호', '영훈']이 나왔습니다.


# 인덱싱을 통해 원소 출력하기 (인덱스는 0부터 시작)
print(numbers[0]) # 모든 리스트의 인덱스는 0부터 셉니다. 따라서 numbers[0]은 첫 번째 원소인 1에 해당합니다.
print(numbers[1]) # numbers[1]은 두 번째 원소이므로 2가 출력됩니다.
print(numbers[0] + numbers[1]) # numbers[0] + numbers[1]은 1 + 2의 결과값 3이 출력됩니다.
print(numbers[5]) # numbers[5]는 여섯 번째 원소, 즉 마지막 원소입니다. 따라서 6이 출력됩니다.

# print(numbers[6])
# numbers[6]는 일곱번째 원소를 가리키는데, 해당 리스트에는 총 여섯 개의 원소밖에 없습니다. 따라서 실행하면 list index out of range라는 오류 메시지가 나옵니다.

# 마이너스 인덱싱
# -1은 리스트 맨 뒤에 원소를 가르킨다
print(names[-1]) # names[-1]은 마지막에서 첫번째 원소, 즉 가장 마지막 원소를 뜻합니다. 따라서 "영훈"이 출력됩니다.
print(names[-2]) # names[-2]는 마지막에서 두번째 원소이므로, "태호"가 출력됩니다.
print(names[-4]) # names[-4]은 마지막에서 네번째 원소, 즉 가장 첫번째 원소에 해당합니다. 따라서 "윤수"가 출력됩니다.
print(numbers[-1]) # 같은 방식으로 numbers[-1]은 가장 마지막 원소입니다. 따라서 6이 출력됩니다.
print(numbers[-2]) # numbers[-2]는 마지막에서 두번째 원소이므로, 5가 출력됩니다.
print(numbers[-6]) # numbers[-6]은 첫번째 원소에 해당하므로, 1이 출력됩니다.


# 슬라이싱 (Slicing)
# 슬라이싱을 통해 원소 출력하기
print(numbers[0:4]) # numbers[0:4]은 인덱스 0부터 3까지 총 4개의 원소이며, 이는 [1, 2, 3, 4]에 해당됩니다.
print(numbers[0:-3]) # numbers[0:-3]은 인덱스 0부터 -4까지, 즉 인덱스 0부터 2까지 총 3개의 원소이며, 이는 [1, 2, 3]에 해당됩니다.
print(numbers[2:]) # numbers[2:]는 인덱스 2부터 마지막 인덱스까지 총 4개의 원소이며, 이는 [3, 4, 5, 6]에 해당됩니다.
print(numbers[:3]) # numbers[:3]은 인덱스 0부터 2까지 총 3개의 원소이며, 이는 [1, 2, 3]에 해당됩니다.


# 원소 바꾸기
# numbers[0] = 7에 의해 리스트의 첫 번째 원소가 7로 바뀝니다. 따라서 [7, 2, 3, 4, 5, 6]이 출력됩니다.
numbers[0] = 7
print(numbers)

#numbers[1] = numbers[1] + numbers[2]에 의해 리스트의 두번째 원소가 리스트의 두번째 원소 2와 세번째 원소 3의 합으로 바뀝니다.
# 즉 numbers[1]이 5가 됩니다.
numbers[1] = numbers[1] + numbers[2]
print(numbers)


# Question: greetings의 원소를 모두 출력해주는 프로그램을 작성해보세요. while문과 리스트의 개념을 활용하시면 됩니다.
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

i = 0

while i < len(greetings):
    print(greetings[i])
    i += 1