# 주민등록번호 YYMMDD-abcdefg는 총 13자리로, 앞의 6자리(YYMMDD)는 생년월일을 의미합니다.
# 문자열 security_number를 파라미터로 받고, security_number의 마지막 네 글자를 '*'로 가린 문자열 값을 리턴해주는 함수
# mask_security_number를 쓰세요. 주민등록번호 가운데에 구분해주는 '-' 작대기 기호가 있든 없든, 아래와 같이 마지막 네 글자가 '*'로 가려져야 합니다.



def mask_security_number(security_number):
    # 코드를 입력하세요.
    pivot = len(security_number) - 4
    until_pivot = security_number[:pivot]
    new_number = until_pivot + "****"
    return new_number

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))