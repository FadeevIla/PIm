def knapsack_recursive(items, capacity):
    n = len(items)

    # Базовый случай: если нет предметов или вместимость рюкзака равна 0, возвращаем 0
    if n == 0 or capacity == 0:
        return 0

    # Если вес последнего предмета больше вместимости рюкзака, рекурсивно вызываем функцию для остальных предметов
    if items[n-1][0] > capacity:
        return knapsack_recursive(items[:n-1], capacity)

    # Рекурсивно вызываем функцию для двух случаев: выбираем последний предмет или не выбираем его
    value_with_item = items[n-1][1] + knapsack_recursive(items[:n-1], capacity - items[n-1][0])
    value_without_item = knapsack_recursive(items[:n-1], capacity)

    # Значение заполнения рюкзака - это максимум между двумя случаями
    return max(value_with_item, value_without_item)


# Пример вызова функции
items = [(5, 10), (3, 5), (2, 8), (7, 14), (4, 7)]  # (вес, стоимость)
capacity = 10

result = knapsack_recursive(items, capacity)
print("Максимальная стоимость заполнения рюкзака:", result)