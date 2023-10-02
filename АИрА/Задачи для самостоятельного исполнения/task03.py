def find_pair(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

# Пример вызова функции
arr = [-2, 0, 3, 5, 7, 9, 12, 15]
target = 10

pair = find_pair(arr, target)
if pair:
    print(f"Найдена пара чисел {pair[0]} и {pair[1]}")
else:
    print("Пара чисел не найдена")