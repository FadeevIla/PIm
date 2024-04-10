import time

# Функция для чтения списка слов из файла
def read_word_list(file_name):
    with open(file_name, encoding='utf-8') as file:
        word_list = [line.strip() for line in file]
    return word_list

# Рекурсивный бинарный поиск с замером времени
def recursive_binary_search_time(word, word_list):
    word_list.sort()
    start_time = time.time()

    def recursive_binary_search(word, word_list, low, high):
        if low > high:
            return False
        mid = (low + high) // 2
        if word_list[mid].lower() == word.lower():
            return True
        elif word_list[mid].lower() < word.lower():
            return recursive_binary_search(word, word_list, mid + 1, high)
        else:
            return recursive_binary_search(word, word_list, low, mid - 1)

    found = recursive_binary_search(word, word_list, 0, len(word_list) - 1)
    end_time = time.time()
    execution_time = end_time - start_time
    return found, execution_time

# Главная функция
def main():
    file_name = input("Введите имя файла со списком слов: ")
    word_list = read_word_list(file_name)
    search_word = input("Введите слово для поиска: ")
    found, time_recursive = recursive_binary_search_time(search_word, word_list)
    if found:
        print(f"Рекурсивный бинарный поиск: слово {search_word} найдено, время исполнения: {time_recursive} секунд")
    else:
        print(f"Рекурсивный бинарный поиск: слово {search_word} не найдено, время исполнения: {time_recursive} секунд")

if __name__ == '__main__':
    main()
