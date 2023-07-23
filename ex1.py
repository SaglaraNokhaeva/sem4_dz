# Напишите функцию для транспонирования матрицы


matrix = input("Введите элементы матрицы через пробел: ").split()
column = input("Введите количество столбцов: ")

print("Исходная матрица: ")
for i in range(0, len(matrix), int(column)):
    for j in range(i, int(column)+i):
        print(matrix[j], " ", end="")
    print()

print("Транспонированная матрица: ")
def transon_matrix(matrix, column):
    for i in range(0, int(column)):
        for j in range(i, len(matrix), int(column)):
            print(matrix[j], " ", end="")
        print()

transon_matrix(matrix, column)


