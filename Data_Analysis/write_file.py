# 파일 열기 'w'는 Write의 약자
out_file = open('write_file.txt', 'w')

# 파일에 쓰기
out_file.write("Hello World!\n")
out_file.write("My name is Kevin")

out_file.close()