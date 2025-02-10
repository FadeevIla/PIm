lst = [1, 2, 3, 4, 5, 8, 9, 11]
elm = 8

def linear_search(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
    return -1, steps


result, steps = linear_search(lst, elm)
print("Алгоритм линейного поиска:")
if result != -1:
    print("Число найдено на позиции", result)
else:
    print("Число не найдено")
print("Количество шагов:", steps)