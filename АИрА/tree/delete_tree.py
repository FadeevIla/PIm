lst = [1, 2, 3, 4, 5, 8, 9, 11]
elm = 8

result, steps = linear_search(lst, elm)
print("Алгоритм линейного поиска:")
if result != -1:
    print("Число найдено на позиции", result)
else:
    print("Число не найдено")
print("Количество шагов:", steps)