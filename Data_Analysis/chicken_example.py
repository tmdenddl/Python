# 매출 파일 열기
# 파일 경로는 "data/chicken.txt" 입니다.

# chicken.txt를 읽어 들이고, strip과 split을 써서 12월 코빠닭의 하루 평균 매출을 계산하세요.
# 평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다. 만약 한 달이 28일이거나 30일이면, 그에 맞게 평균 매출을 구할 수 있도록 코드를 짜셔야 합니다.
month = open('data/chicken.txt', 'r')

sum = 0
days = 0
for day in month:
    data = day.split("일: ")
    days += 1
    sum += int(data[1])

avg = sum / days
print(avg)
# 파일 닫기
month.close()