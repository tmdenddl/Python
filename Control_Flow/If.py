temperature = 15

# 온도가 20도 이상일 경우 자켓을 입지 말고 20도 이하일 경우 자켓을 입으시
if temperature >= 20:
    print("자켓을 입지 마세요")
else:
    print("자켓을 입으세요")

# 다양한 경우가 주어질 때
if temperature < 5:
    print("코트를 챙기세요")
elif temperature < 10:
    print("자켓을 챙기세요")
elif temperature < 15:
    print("가디건을 챙기세요")
elif temperature < 20:
    print("긴팔을 입으세요")
else:
    print("반팔을 입으세요")