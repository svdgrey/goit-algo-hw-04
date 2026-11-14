
# Сортує масив за допомогою сортування злиттям (merge sort)
# - arr: список чисел для сортування
# Повертає відсортований список чисел
def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


# Зливає два відсортовані масиви в один відсортований масив
# - left: відсортований список чисел
# - right: відсортований список чисел
# Повертає відсортований список чисел, що є результатом злиття left і right
def merge(left: list[int], right: list[int]) -> list[int]:
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged
