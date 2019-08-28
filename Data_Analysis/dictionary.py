# 사전 = dictionary
# key - value

dict_1 = {}

# <class 'dict'>
print(type(dict_1))

dict_1[5] = 25 # {5: 25} = {key: value}
dict_1[2] = 4 # {2: 4}
dict_1[3] = 9 # {3: 9}

# key의 값을 기준으로 나열된다
print(dict_1)

# key와 연결된 value값을 출력한다
print(dict_1[3])


# 그럼 key가 정수형인 사전과 그냥 리스트의 차이점은 뭘까요?
# 리스트는 인덱스 0부터 시작하고 순서대로 채워지지만 사전은 순서가 없기때문에 0부터 시작하지 않고 아무 값들을 쓸 수 있습니다.
# 사전이 리스트와 가장 다른 점은 key가 정수뿐만 아니라 아무 자료형이나 될 수 있다는 것입니다.
family = {}

family['Mother'] = 'Lynn'
family['Father'] = 'Lee'
family['Son'] = 'Kevin'
family['Daughter'] = 'Jessica'

# Kevin을 출력한
print(family['Son'])

# key값들만 받아오기
print(family.keys())
# key값들을 리스트로 받아오기
print(list(family.keys()))

# family의 key값 확인하기
print('Son' in family)

# value값들만 받아오기
print(family.keys())
# value값들을 리스트로 받아오기
print(list(family.keys()))

# family의 value값 확인하기
print('Kevin' in family.values())