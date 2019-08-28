from random import randint


# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    # 숫자를 저장할 리스트
    numbers = []

    # 6가지 숫자 뽑기
    draw = 0
    while draw < 6:
        number = randint(1, 45)
        if number not in numbers:
            numbers.append(number)
            draw += 1

    # 숫자들을 오름차순으로 정렬
    numbers.sort()
    return numbers


# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    # 숫자를 저장할 리스트
    winning_numbers = generate_numbers()

    # 보너스 숫자 뽑기
    while len(winning_numbers) < 7:
        bonus = randint(1, 45)
        if bonus not in winning_numbers:
            winning_numbers.append(bonus)

    return winning_numbers


# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    # 숫자 카운트
    count = 0

    for num_A in list1:
        if num_A in list2:
            count += 1

    return count


# 로또 등수 확인하기
def check(numbers, winning_numbers):
    # 보너스를 제외하고 몇개를 맞췄는가
    correct = count_matching_numbers(numbers, winning_numbers[:6])

    # 등수 정하기
    if correct == 3:  # 3개를 맞춘경우 (5등)
        return 5000
    elif correct == 4:  # 4개를 맞춘경우 (4등)
        return 50000
    elif correct == 5 and winning_numbers[6] not in numbers:  # 5개를 맞추고 보너스를 못 맞춘 경우 (3등)
        return 1000000
    elif correct == 5 and winning_numbers[6] in numbers:  # 5개 + 보너스를 맞춘 경우 (2등)
        return 50000000
    elif correct == 6:  # 6개를 맞춘경우 (1등)
        return 1000000000
    else:
        return 0
