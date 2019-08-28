# 선택 정렬
def selection_sort(my_list):
    # 코드를 입력하세요.
    # 바깥 반복문
    for i in range(len(my_list)):
        min_index = i

        # 안쪽 반복문
        for j in range(i + 1, len(my_list)):
            value = my_list[j]
            if value < my_list[min_index]:
                min_index = j

        # 자리 바꾸기
        min_value = my_list[min_index]
        my_list[min_index] = my_list[i]
        my_list[i] = min_value

    return my_list


some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)