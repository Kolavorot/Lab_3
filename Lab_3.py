#8.	Формируется матрица F следующим образом: если в С количество простых чисел в нечетных столбцах в области 2 больше,
# чем количество нулевых  элементов в четных строках в области 3, то поменять в С симметрично области 1 и 3 местами,
# иначе С и В поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение:
# ((К*A)*F– (K * A^T) .
# Выводятся по мере формирования А, F и все матричные операции последовательно.


import random

K_test = 3  # Тестовые данные
N_test = 10
E_test = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]]

B_test = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]]

C_test = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1]]

D_test = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]]

print('Использовать тестовые данные или случайные?')
while True:
    choice = input(
        'Введите 1, если хотите использовать тестовые данные, 2 - если случайные, q - для выхода из программы): ')
    if choice == '1' or choice == '2' or choice == 'q':
        break

if choice == '1':
    K = K_test
    N = N_test
    B, C, D, E = B_test, C_test, D_test, E_test
    n = N // 2   # Размерность матриц B, C, D, E (n x n)

if choice == '2':  # Генерация случайных данных
    K = int(input("Введите число К="))
    while True:
        N = int(input("Введите число n="))
        if N < 6:
            print('Число N слишком малое. Введите N >= 6')
        else:
            break
    B, C, D, E = [], [], [], []
    n = N // 2  # Размерность матриц B, C, D, E (n x n)
    for row in range(n):
        row_b, row_c, row_d, row_e = [], [], [], []
        for col in range(n):
            row_b.append(random.randint(-10, 10))
            row_c.append(random.randint(0, 1))
            row_d.append(random.randint(-10, 10))
            row_e.append(random.randint(-10, 10))
        B.append(row_b)
        C.append(row_c)
        D.append(row_d)
        E.append(row_e)

if choice == 'q':
    exit()

if N % 2 == 0:
    print("Число N чётное, в итоговой матрице А будут обрабатываться все элементы")
else:
    print(
        f'Число N нечётное, в итоговой матрице А не будут обрабатываться элементы {N // 2 + 1} строки и столбца, т.к. они не входят в подматрицы')

A = []
for row in range(n):
    A.insert(row, E[row] + B[row])
    A.insert(row + n, D[row] + C[row])

# Печатаем матрицы E, B, C, D, A
print('Матрица E:')
for row in range(n):
    print(E[row])

print('Матрица B:')
for row in range(n):
    print(B[row])

print('Матрица C:')
for row in range(n):
    print(C[row])

print('Матрица D:')
for row in range(n):
    print(D[row])

print('Матрица A:')
for row in range(len(A)):
    print(A[row])

# Проверяем число на простоту
def issimple(n):
    k = 0
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
            k = k + 1
    if (k <= 0):
        return n


# Считаем количество простых чисел в нечетных столбцах в области 2 в матрице C
count_more_K = 0
N = len(C)
mid = N // 2
is_even = N % 2 == 0
for col in range(mid, N):
    for row in range(0, N):
        if is_even and (abs(col - mid) <= abs(mid - row) or abs(col - mid + 1) <= abs(mid - row))\
                or not is_even and abs(col - mid) <= abs(mid - row):
            if (col + 1) % 2 != 0:
                if issimple(C[row][col]):
                     count_more_K += 1

# Считаем количество нулевых чисел в чётных строках в области 3 в матрице С
count_more_1_K = 0
for row in range(mid, N):
    for col in range(0, N):
        if is_even and (abs(col - mid) <= abs(mid - row) or abs(col - mid + 1) <= abs(mid - row))\
                or not is_even and abs(col - mid) <= abs(mid - row):
            if (row + 1) % 2 == 0: # Нумерация строк начинается с 1
                print(C[col][row],col,row)
                if C[row][col] == 0:
                    count_more_1_K += 1  # Увеличиваем счетчик
print(count_more_1_K)
exit()

F = []  # Создаём матрицу F следующим образом
if count_more_K > count_more_1_K:  # Если в C количество простых чисел в нечетных столбцах в области 2 больше,
    C_F = C
    for row in range(1, n // 2 + 1):
        for col in range(row, n - row):
            C_F[row - 1][col], C_F[col][row - 1] = C_F[col][row - 1], C_F[row - 1][col]
    print('Матрица F')
    for row in range(n):
        F.insert(row, E[row] + B[row])
        F.insert(row + n, D[row] + C_F[row])
    for row in range(len(F)):
        print(F[row])
else:  # иначе С и В поменять местами несимметрично
    for row in range(n):
        F.insert(row, E[row] + B[row])
        F.insert(row + n, D[row] + C[row])
    print('Матрица F:')
    for row in range(len(F)):
        print(F[row])

# Выражение -------------------------------------------

A_transpose = []  # Транспонируем матрицу A
for row in range(len(A)):
    A_transpose_row = []
    for col in range(len(A)):
        A_transpose_row.append(A[col][row])
    A_transpose.append(A_transpose_row)

print('Транспонированная матрица A:')
for row in range(len(A)):
    print(A_transpose[row])

A_and_K = []  # Умножаем матрицу A на константу K
for row in range(len(A)):
    cur_row = []
    for col in range(len(A)):
        cur_row.append(0)
    A_and_K.append(cur_row)  # формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам

for row in range(len(A)):
    for col in range(len(A)):
        A_and_K[row][col] = K * A[row][col]

print('Матрица A*K:')
for row in range(len(A)):
    print(A_and_K[row])


A_and_K_and_F = []  # Умножаем матрицы (A*K) * F
for row in range(len(A_and_K)):
    F_row = []
    for i in range(len(A_and_K)):
        sum = 0
        for j in range(len(A_and_K)):
            sum += A_and_K[row][j] * F[j][i]
        F_row.append(sum)
    A_and_K_and_F.append(F_row)

print('Матрица (A*K)*F:')
for row in range(len(A)):
    print(A_and_K_and_F[row])

AT_and_K = [] # Умножаем транспонированную матрицу A на константу K
for row in range(len(A_transpose)):
    cur_row = []
    for col in range(len(A_transpose)):
        cur_row.append(0)
    AT_and_K.append(cur_row)  # формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам

for row in range(len(A_transpose)):
    for col in range(len(A_transpose)):
        AT_and_K[row][col] = K * A_transpose[row][col]

print('Матрица AT*K:')
for row in range(len(A_transpose)):
    print(A_and_K[row])
result_matrix = []  # Результирующая матрица(разность ((К*A)*F– (K * A^T)
for row in range(len(A)):  # Формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам
    cur_row = []
    for col in range(len(A)):
        cur_row.append(0)
    result_matrix.append(cur_row)

for row in range(len(A)):
    for col in range(len(A)):
        result_matrix[row][col] = A_and_K_and_F[row][col] - AT_and_K[row][col]

print('Результат:')
for row in range(len(result_matrix)):
    print(result_matrix[row])
