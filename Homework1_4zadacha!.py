# Anatoli Gytovski
# Date: 18/02/2024
# Description: Homework 2_zadacha4
# Grodno IT Academy Python 3.11.7


# добавьте в репозиторий с домашним задание файл readme.md с датой сдачи, фамилией и именем выполнившего и кратким
# описанием каждой задачи (коротко, что использовали, алгоритм функции), оформленным в стиле markdown


# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

def uniques(repeating_string):
    repeating_string = repeating_string.replace(
        " ", "")   # Удаляем все пробелы из строки
    unique_chars = ""
    for char in repeating_string:        # Пройдемся по каждому символу
        if char not in unique_chars:
            unique_chars += char
    return unique_chars


input_string = input("Введите строку: ")
result = uniques(input_string)
print(result)


# В данном коде функция uniques() принимает введенную строку, удаляет из нее все пробелы и затем проходится по каждому символу.
# Если символ еще не встречался в строке unique_chars, то он добавляется к ней.
# Таким образом, после завершения цикла в unique_chars останутся только уникальные символы.
# После выполнения кода программа попросит ввести строку, а затем выведет результат без повторяющихся символов и пробелов.
