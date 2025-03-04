def knapsack_greedy_binary(items, capacity):
    n = len(items)

    # Сортируем предметы по убыванию их стоимости
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    # Создаем список для хранения выбранных предметов и общей стоимости
    selected_items = [0] * n
    total_value = 0

    for i, item in enumerate(sorted_items):
        if capacity >= item[0]:  # Проверяем, влезает ли предмет в рюкзак
            selected_items[i] = 1
            total_value += item[1]
            capacity -= item[0]

    return selected_items, total_value

# Пример вызова функции
items = [(5, 10), (3, 5), (2, 8), (7, 14), (4, 7)] # (вес, стоимость)
capacity = 10

selected_items, total_value = knapsack_greedy_binary(items, capacity)
print("Выбранные предметы:")
for i, item in enumerate(selected_items):
    if item:
        print(f"Вес: {items[i][0]}, Стоимость: {items[i][1]}")
print(f"Общая стоимость: {total_value}")