#자연수 중 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 프로그램을 써보세요. 아래처럼 콘솔에 출력되면 됩니다.

i = 1
n = 120
count = 0

while i <= n:
    if n%i== 0:
            print(i)
            count = count + 1
    i = i + 1

print("%d의 약수는 총 %d개입니다." % (n, count))