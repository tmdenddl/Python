# User라는 새로운 클래스를 정의
class User:

    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # 좀 더 효율적인 init method
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def say_my_name(self):
        print("My name is " + self.name)

    # 자기 소개 (이름, 이메일)
    def introduce(self):
        print("My name is %s" % self.name)
        print("My email address is %s" % self.email)

    # 자기 소개 두번
    def introduce_twice(self):
        self.introduce()
        self.introduce()


# user1,2라는 User클래스의 Instance를 생성
user1 = User()
user2 = User()

# <class '__main__.User'> main에 있는 User클래스
print(type(user1))
print(type(user2))

print(user1 == user2)  # 둘은 다른 instance이기 때문에 False

user2 = user1  # user2가 user1의 instance를 가르킨다

print(user1 == user2)  # user1 과 user2가 같은 instance를 가르키기 때문에 True

#######################################################################################################################
user1 = User()
user2 = User()

user1.name = "Kevin"
user1.email = "kevin@gmail.com"
user1.password = "123456"

user2.name = "Emily"
user2.email = "Emily@gmail.com"
user2.password = "abcdef"

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)

# 같은 식 다른 방식
User.say_my_name(user1)  # Class.Method(Instance)
user1.say_my_name()  # Instance.Method()

user3 = User()
user3.initialize("JYP", "jyp@gmail.com", "jpy123")

user4 = User("YG", "yg@gmail.com", "YG123")
