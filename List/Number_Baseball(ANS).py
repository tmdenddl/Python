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


# 번호 뽑기
def generate_numbers():
    # 숫자 3개를 보관할 리스트 생성
    numbers = []

    # 3개의 요소가 있을때까지 반복
    while len(numbers) < 3:
        # 새로 뽑은 수가 numbers에 없을 경우에만 추가
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    # 리스트 리턴
    return numbers


# 정답 뽑기
ANSWER = generate_numbers()

# 변수 초기값 설정
tries = 0  # 시도 횟수
strike_count = 0  # 스트라이크 개수
ball_count = 0  # 볼 개수

# 번호를 모두 맞출때까지 반복
while strike_count < 3:
    # 번호 3개 입력 받기
    guess = []
    while len(guess) < 3:
        # 새로 입력한 수가 guess에 없을 경우에만 추가
        new_number = int(input("%d번째 수를 입력하세요: " % (len(guess) + 1)))

        # 범위를 벗어나면 설명 메시지 출력
        if new_number < 0 or new_number > 9:
            print("0에서 9까지의 수를 입력해주세요!")
        # 중복된 수를 입력하면 설명 메시지 출력
        elif new_number in guess:
            print("새로운 수를 입력해주세요!")
        # 타당한 값이면 guess에 추가
        else:
            guess.append(new_number)

    # 스트라이크, 볼 개수 세기
    strike_count = 0  # 스트라이크 개수
    ball_count = 0  # 볼 개수
    i = 0  # 인덱싱 변수

    while i < 3:
        if guess[i] == ANSWER[i]:
            strike_count = strike_count + 1
        elif guess[i] in ANSWER:
            ball_count = ball_count + 1
        i = i + 1

    print("%dS %dB" % (strike_count, ball_count))

    # 시도 횟수 추가
    tries = tries + 1

# 축하 메시지
print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (tries))
