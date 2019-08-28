# split 메소드는 파라미터로 넘겨주는 값을 기준으로 문자열을 분리시키고, 분리된 값들이 정리되어 있는 리스트를 리턴해줍니다.

numbers = "1. 2. 3. 4. 5. 6"

# split은 parameter에 들어가는 값을 기준으로 문자열을 나누어 리스트로 저장한
print(numbers.split("."))

# 띄어쓰기를 없애고 싶을때
print(numbers.split(". "))

# Example
full_name = "Lee, Seungwook"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]

print(last_name)
print(first_name)

# 화이트 스페이스를 기반으로 나누고 싶을시 parameter에 값을 넣지 말자
some_string = "  ab  cd  -  e   fgh  \n"
print(some_string.split())