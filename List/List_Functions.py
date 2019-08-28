numbers = []

# 리스트의 길이(0)를 출력해줍니다
print(len(numbers))

# 리스트에 값을 더해줍니다
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

# 리스트의 길이(5)를 출력해줍니다
print(len(numbers))

# 리스트 인덱스 3에 위치한 값을 지워줍니다
del numbers[3]
print(numbers)

# 리스트 인덱스 5에 0의 값을 더해줍니다
numbers.insert(5, 0)
print(numbers)

# 리스트의 값을 정렬해서 출력합니다
print(sorted(numbers))