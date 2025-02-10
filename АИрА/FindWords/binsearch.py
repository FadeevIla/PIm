import time

# Функция для чтения списка слов из файла
def read_word_list(file_name):
    with open(file_name, encoding='utf-8') as file:
        word_list = [line.strip() for line in file]
    return word_list

# Бинарный поиск с замером времени
def binary_search_time(word, word_list):
    start_time = time.time()
    found = False
    low = 0
    high = len(word_list) - 1

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

# Главная функция
def main():
    file_name = input("Введите имя файла со списком слов: ")
    word_list = read_word_list(file_name)

    search_word = input("Введите слово для поиска: ")

    found, time_binary = binary_search_time(search_word, word_list)
    if found:
        print(f"Бинарный поиск: слово {search_word} найдено, время исполнения: {time_binary} секунд")
    else:
        print(f"Бинарный поиск: слово {search_word} не найдено, время исполнения: {time_binary} секунд")

if __name__ == '__main__':
    main()