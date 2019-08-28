# 리스트 뒤집기
numbers = [2, 4, 6, 8, 10, 12, 14]

# 위와 같이 numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집어 아래의 내용이 출력되게 하세요.
for left_index in range(int(len(numbers) / 2)):
    # 오른쪽 인덱스 계산
    right_index = len(numbers) - left_index - 1

    # 원소 바꾸기
    temp = numbers[left_index]
    numbers[left_index] = numbers[right_index]
    numbers[right_index] = temp

print("뒤집어진 리스트: " + str(numbers))