# Напишите функцию для транспонирования матрицы

column, line = input("Введите количество столбцов и строк через пробел: ").split()
matrix = input("Введите элементы матрицы через пробел: ").split()
# print(column, line)
# print(type(column))
# print(type(line))


for i in range(len(matrix)):
    _ = 0
    for j in range((i + _), int(column)):
        print(matrix[j])
    _ += int(column)
    print("\n")

# def transon_matrix(matrix, column, line)
