# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
# 코드를 입력하세요
i = 0
while i < 10:
    i += 1
    numbers.append(i)

print(numbers)




# numbers에서 홀수 제거
# 코드를 입력하세요
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else:
        i += 1

print(numbers)




# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)
print(numbers)




# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers = sorted(numbers)
print(numbers)




# 리스트에서 값의 존재 확인하기
# 어떤 값이 리스트에 있는지 확인하는 함수를 써보겠습니다.
# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))


# 똑같은 식이지만 in이라는 함수를 사용하면 더 쉽다
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)


# 원소가 없다는것을 확인할 때에는 not in을 활용
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 not in primes)
print(12 not in primes)




# 리스트 안의 리스트 (Nested List)
# 리스트 안에는 또 다른 리스트가 있을 수 있습니다. 이를 영어로 nested list라고 부릅니다.

# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)





# sort 메소드
# 저번에 정렬된 새로운 리스트를 리턴시켜주는 sorted 함수를 보여드렸습니다.
# some_list.sort()는 새로운 리스트를 생성하지 않고 some_list를 정렬된 상태로 바꿔줍니다.
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)




# reverse 메소드
# some_list.reverse()는 some_list의 원소들을 뒤집어진 순서로 배치합니다.
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)




# index 메소드
# some_list.index(x)는some_list에서 x의 값을 갖고 있는 원소의 인덱스를 리턴해줍니다.
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))




# remove 메소드
# some_list.remove(x)는some_list에서 첫 번째로 x의 값을 갖고 있는 원소를 삭제해줍니다.
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)