def binary_search(element, some_list):
    # 인덱스 중간 값
    start = 0
    end = len(some_list) - 1

    while start <= end:
        middle = (start + end) // 2

        if some_list[middle] == element:
            return middle
        elif some_list[middle] < element:
            start = middle + 1
        elif some_list[middle] > element:
            end = middle - 1

    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

print()


# Using Recursive Functions
def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index is None:
        end_index = len(some_list) - 1
    elif start_index > end_index:
        return None

    mid_index = (end_index + start_index) // 2

    if some_list[mid_index] == element:
        return mid_index
    elif some_list[mid_index] > element:
        end_index = mid_index - 1
        return binary_search(element, some_list, start_index, end_index)
    elif some_list[mid_index] < element:
        start_index = mid_index + 1
        return binary_search(element, some_list, start_index, end_index)

    # 코드를 작성하세요.


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
