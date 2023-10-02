import time

# Функция для чтения списка слов из файла
def read_word_list(file_name):
    with open(file_name, encoding='utf-8') as file:
        word_list = [line.strip() for line in file]
    return word_list

# Линейный поиск с замером времени
def linear_search_time(word, word_list):
    start_time = time.time()

    found = False
    for w in word_list:
        if w == word:
            found = True
            break

    end_time = time.time()
    execution_time = end_time - start_time
    return found, execution_time

# Бинарный поиск с замером времени
def binary_search_time(word, word_list):
    start_time = time.time()

    low = 0
    high = len(word_list) - 1
    found = False

    while low <= high:
        mid = (low + high) // 2
        if word_list[mid] == word:
            found = True
            break
        elif word_list[mid] < word:
            low = mid + 1
        else:
            high = mid - 1

    end_time = time.time()
    execution_time = end_time - start_time
    return found, execution_time

# Рекурсивный поиск с замером времени
def recursive_search_time(word, word_list):
    start_time = time.time()

    def recursive_search(word, word_list):
        if not word_list:
            return False

        mid = len(word_list) // 2
        if word_list[mid] == word:
            return True
        elif word_list[mid] < word:
            return recursive_search(word, word_list[mid + 1:])
        else:
            return recursive_search(word, word_list[:mid])

    found = recursive_search(word, word_list)

    end_time = time.time()
    execution_time = end_time - start_time
    return found, execution_time

# Главная функция
def main():
    file_name = input("Введите имя файла со списком слов: ")
    word_list = read_word_list(file_name)

    search_word = input("Введите слово для поиска: ")

    found_linear, time_linear = linear_search_time(search_word, word_list)
    found_binary, time_binary = binary_search_time(search_word, word_list)
    found_recursive, time_recursive = recursive_search_time(search_word, word_list)

    if found_linear:
        print(f"Линейный поиск: слово {search_word} найдено, время исполнения: {time_linear} секунд")
    else:
        print(f"Линейный поиск: слово {search_word} не найдено, время исполнения: {time_linear} секунд")

    if found_binary:
        print(f"Бинарный поиск: слово {search_word} найдено, время исполнения: {time_binary} секунд")
    else:
        print(f"Бинарный поиск: слово {search_word} не найдено, время исполнения: {time_binary} секунд")

    if found_recursive:
        print(f"Рекурсивный поиск: слово {search_word} найдено, время исполнения: {time_recursive} секунд")
    else:
        print(f"Рекурсивный поиск: слово {search_word} не найдено, время исполнения: {time_recursive} секунд")

if __name__ == '__main__':
    main()