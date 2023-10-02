lst = [1, 2, 3, 4, 5, 8, 9, 11]
elm = 8

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    steps = 0
    
    while left <= right:
        middle = (left + right) // 2
        steps += 1
        if arr[middle] == target:
            return middle, steps
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    
    return -1, steps


result, steps = binary_search(lst, elm)
print("Алгоритм бинарного поиска:")
if result != -1:
    print("Число найдено на позиции", result)
else:
    print("Число не найдено")
print("Количество шагов:", steps)