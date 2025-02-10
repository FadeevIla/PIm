lst = [1, 2, 3, 4, 5, 8, 9, 11]
elm = 8

def binary_search_recursive(arr, target, left, right, steps=0):
    if left > right:
        return -1, steps

    middle = (left + right) // 2
    steps += 1
    if arr[middle] == target:
        return middle, steps
    elif arr[middle] < target:
        return binary_search_recursive(arr, target, middle + 1, right, steps)
    else:
        return binary_search_recursive(arr, target, left, middle - 1, steps)


result, steps = binary_search_recursive(lst, elm, 0, len(lst) - 1)
print("Алгоритм бинарного поиска - рекурсивно:")
if result != -1:
    print("Число найдено на позиции", result)
else:
    print("Число не найдено")
print("Количество шагов:", steps)