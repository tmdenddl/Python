# print문 자체에서도 enter가 들어가지만 \n 자체도 enter를 뜻해 enter가 총 두번 눌리게 된다.
print("Hello World\n")
print("Hello World")

# strip()은 화이트 스페이스를 없애준다
print("    abc    def    ".strip())