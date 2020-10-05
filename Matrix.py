import numpy as np
import copy


def minor(B, i, j):
    M = copy.deepcopy(B)
    del M[i]
    n = len(M[0])
    if n == 1:
        return M
    else:
        for i in range(len(B[0]) - 1):
            del M[i][j]
        return M


def det(A):
    n = len(A[0])
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0
    for j in range(n):
        determinant += A[0][j] * signum * det(minor(A, 0, j))
        signum *= -1
    return determinant


while True:
    print('Введите размер квадратной матрицы')
    try:
        r = int(input())
        break
    except(ValueError, TypeError):
        print('Размер матрицы - целое число')

a = 0

while True:
    if (a == 1) or (a == 2):
        print('Выполнение...')
        break
    else:
        try:
            print('Способ заполнения:\n1) Автоматически\n2) Вручную')
            a = int(input())
        except (TypeError, ValueError):
            print('Этого нет в списке вариантов')

if a == 1:
    print('Введите минимальное число диапазона')
    while True:
        try:
            minim = int(input())
            break
        except(TypeError, ValueError):
            print('Введите целое число')
    print('Введите максимальное число диапазона')
    while True:
        try:
            maxim = int(input())
            break
        except(TypeError, ValueError):
            print('Введите целое число')
    matrix = []

    for f in range(r):
        matrix.append([])
        for s in range(r):
            matrix[f].append(np.random.randint(minim, maxim))

else:
    matrix = []
    for f in range(r):
        matrix.append([])
        for s in range(r):
            print('Введите элемент a', f + 1, s + 1, sep='')
            while True:
                try:
                    matrix[f].append(float(input()))
                    break
                except (TypeError, ValueError):
                    print('Введите число')

print('Ваша матрица:')
for f in range(r):
    print('|', end=' ')
    for s in range(r):
        print(matrix[f][s], end=' ')
    print('|')

print('Вычисление определителя...')
print('Определитель матрицы равен', det(matrix))
