def merge(list1, list2):
    new_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1

    # list1에 남은 원소가 있다면, new_list에 추가하기
    while i < len(list1):
        new_list.append(list1[i])
        i += 1

    # list2에 남은 원소가 있다면, new_list에 추가하기
    while j < len(list2):
        new_list.append(list2[j])
        j += 1

    return new_list


# 합병 정렬
def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        # 리스트를 반으로 나눠주기
        left = my_list[:len(my_list) // 2]
        right = my_list[len(my_list) // 2:]

        # 반으로 나눈 리스트를 정렬하기
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)

        # 정렬된 나뉜 리스트를 합치기
        return merge(sorted_left, sorted_right)


some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)