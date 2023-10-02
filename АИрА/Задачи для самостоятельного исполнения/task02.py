def minimum_squares(side1, side2):
    if side1 == 0 or side2 == 0:
        return 0
    elif side1 == side2:
        return 1
    else:
        min_squares = float('inf')
        for i in range(1, min(side1, side2) + 1):
            squares = minimum_squares(side1 - i, side2) + minimum_squares(i, side2 - i)
            if squares < min_squares:
                min_squares = squares
        return min_squares

# Ввод сторон прямоугольника
side1 = 5
side2 = 3

result = minimum_squares(side1, side2)
print(f"Минимальное количество квадратов: {result}")