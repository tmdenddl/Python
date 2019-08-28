# Initialize i
i = 1

# Execute 3 times
while i <= 3:
    print("I can code too!")
    i = i + 1

# Is n even?
def is_even(n):
    return ((n%2) == 0)


# Print all even numbers from 1 ~ 100
i = 1
while i <= 100:
    if is_even(i):
        print(i)
    i = i + 1



# while문과 if문을 활용하여 100이하의 자연수 중 8의 배수이지만, 12의 배수는 아닌 것을 모두 출력하세요. 실행하면 아래의 내용이 콘솔에 출력되어야 합니다.

i = 8
while i <= 100:
    if (i % 12 != 0):
        print(i)
    i = i + 8


# while문과 if문을 활용하여, 1000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써보세요.

i = 1
sum = 0

while i < 1000:
    if (i%2 == 0 or i%3 == 0):
        sum = sum + i
    i = i + 1

print(sum)