# 피보나치 수열이란 첫 번째 항과 두 번째 항이 1이고, 세 번째 항부터는 바로 앞의 두 항의 합으로 정의된 수열입니다.
# 예를 들어서 세 번째 항은 첫 번째 항(1)과 두 번째 항(1)을 더한 2이며, 네 번째 항은 두 번째 항(1)과 세 번째 항(2)을 더한 3이 될 것입니다.
previous = 0
current = 1
i = 0

while i < 20:
    print(current)
    temp = previous
    previous = current
    current = current + temp
    i += 1
