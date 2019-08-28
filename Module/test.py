# from 모듈 파일의 이름 import 불러올 변수/함수/클래스

# calculator.py에서 sum 함수 불러오기
# from Calculator import sum

# 만약 모듈에 정의된 모든 변수, 함수, 클래스를 호출하려면 어떻게 할까요?
#from calculator import sum, difference, product, square

# *를 쓰면, 모듈 안에 정의된 모든 변수/함수/클래스를 불러올 수 있습니다.
from calculator import *

print(sum(3, 5))
print(difference(3, 5))
print(product(3, 5))
print(square(3))

print(sum(3, 5))