# 리스트
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

print(alphabets_list[0]) # A
print(alphabets_list[1]) # B
print(alphabets_list[4]) # E
print(alphabets_list[-1]) # J

print(alphabets_list[0:5]) # ['A', 'B', 'C', 'D', 'E']
print(alphabets_list[4:]) # ['E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[:4]) # ['A', 'B', 'C', 'D']

# 문자열
alphabets_string = 'ABCDEFGHIJ'

print(alphabets_string[0]) # A
print(alphabets_string[1]) # B
print(alphabets_string[4]) # E
print(alphabets_string[-1]) # J

print(alphabets_string[0:5]) # ABCDE
print(alphabets_string[4:]) # EFGHHIJ
print(alphabets_string[:4]) # ABCD



# Exercise
# 파라미터로 정수형 num의 값을 받는 sum_digit 함수를 쓰세요. sum_digit은 num의 각 자리수를 더한 값을 리턴해주는 역할을 합니다.

# 자리수 합 리턴
def sum_digit(num):
    # 코드를 입력하세요.
    str_num = str(num)  # 정수형 -> 문자열
    sum = 0
    for digit in str_num:  # 각 자리의 숫자를
        sum += int(digit)  # 더하시오

    return sum


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
total = 0
for i in range(1, 1001):
    total += sum_digit(i)

print(total)