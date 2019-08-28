# 숫자 맞추기 게임에 이어, 숫자 야구 게임을 만들려고 합니다. 룰은 다음과 같습니다.
#
# 컴퓨터는 0과 9 사이의 서로 다른 세 숫자를 임의의 순서로 뽑습니다. 사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추려고 합니다.
#
# 컴퓨터는 사용자가 입력한 세 숫자에 대해서, 아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려줍니다.
#
# 숫자의 값과 위치가 모두 일치하면 S입니다.
# 숫자의 값은 일치하지만 위치가 틀렸으면 B입니다.
# 예를 들어 컴퓨터가 1, 2, 3을 생성하였는데, 사용자가 1, 3, 5를 입력하면, 1S(1의 값과 위치가 일치) 1B(3의 값만 일치)입니다.
# 기회는 무제한입니다. 하지만 몇번의 시도 끝에 맞췄는지 기록됩니다.
#
# 3S(세 숫자의 값과 위치를 모두 맞춘 경우)일 때 게임이 끝납니다.

from random import randint

numbers = []

# 서로 다른 세 숫자를 임의의 순서로 뽑기
numbers_to_select = 0
while numbers_to_select < 3:
    num = randint(0, 9)
    if num not in numbers:
        numbers.append(randint(0, 9))
        numbers_to_select += 1

print(numbers)

# 게임 시작
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
tries = 1
# 무한루프
while tries > 0:
    strike = 0
    ball = 0
    print("세 수를 하나씩 차례대로 입력하세요.")

    no_tries = 0
    guesses = []
    while no_tries < 3:  # 숫자 세개 지정
        num = int(input("%d번째 수를 입력하세요: " % (no_tries + 1)))
        if num < 0 or num > 9:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            continue
        if num in guesses:
            print("중복되는 수 입니다. 다시 입력해주세요.")
        else:
            guesses.append(num)
            no_tries += 1

    no_tries = 0
    while no_tries < 3:  # 지정한 세개의 숫자값을 비교
        num = guesses[no_tries - 1]
        if num == numbers[no_tries - 1]:
            strike += 1
        elif num in numbers:
            ball += 1
        no_tries += 1

    if strike == 3:  # 결과
        print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % tries)
        break  # 성공할 경우에만 조건문을 나가시오

    print("%dS, %dB" % (strike, ball))
    tries += 1
