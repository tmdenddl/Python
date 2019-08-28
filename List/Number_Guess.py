from random import randint

# 숫자
ANSWER = randint(1, 20)
print(ANSWER)

# try = 기회 횟수
tries = 0
correct = False

# 기회가 0번이 될때까지 반복
while tries < 4:
    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (4 - tries)))
    tries += 1
    if ANSWER > guess:  # 입력한 값이 숫자보다 작을 경우
        print("Up")
    elif ANSWER < guess: # 입력한 값이 숫자보다 클 경우
        print("Down")
    else:  # 맞출 경우
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % tries)
        correct = True
        break


if correct == False: # 주어진 기회를 다 쓴 경우
    print("아쉽습니다. 정답은 %d였습니다." % (ANSWER))

