# Напишите функцию для транспонирования матрицы

column, line = input("Введите количество столбцов и строк через пробел: ").split()
matrix = input("Введите элементы матрицы через пробел: ").split()

print("Исходная матрица: ")
for i in range(0, len(matrix), int(column)):
    for j in range(i, int(column)+i):
        print(matrix[j], " ", end="")
    print()

print("Транспонированная матрица: ")
def transon_matrix(matrix, column, line):
    for i in range(0, int(column)):
        for j in range(i, len(matrix), int(column)):
            print(matrix[j], " ", end="")
        print()

transon_matrix(matrix, column, line)


