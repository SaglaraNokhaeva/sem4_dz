# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

starting_dict = {}

while 1:
    str = input("Введите ключ и значение через '=', для заверешния ввода введите пустую строку: ")
    if str == '':
        break
    key, value = str.split('=')
    starting_dict[key] = value

print("Исходный словарь: ", starting_dict)


def transpose(start_dict):
    transpon_dict = {}
    for key, value in start_dict.items():
        transpon_dict[value] = key
    return transpon_dict


print("Транспонированный словарь: ", transpose(starting_dict))
