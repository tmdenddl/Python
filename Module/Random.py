from random import randint, uniform

# 1부터 45사이의 정수를 프린트
print(randint(1, 45))

# 1부터 45사이의 소수를 프린트
print(uniform(1, 45))

# 로또 자동
numbers = []

i = 0
while i < 6:
    number = randint(1, 45)
    if number not in numbers:
        numbers.append(number)
        print(number)
        i = i + 1
