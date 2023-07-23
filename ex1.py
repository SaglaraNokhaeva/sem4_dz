# Напишите функцию для транспонирования матрицы

column, line = input("Введите количество столбцов и строк через пробел: ").split()
matrix = input("Введите элементы матрицы через пробел: ").split()
# print(column, line)
# print(type(column))
# print(type(line))


for i in range(0, len(matrix), 2):
    # print(i)
    # print(len(matrix), int(column))
    # _ = 0
    for j in range(i, int(column)):
        # print(j, int(column))
        print(matrix[j], end="")
    # _ += int(column)
    print("\n")

# def transon_matrix(matrix, column, line)
