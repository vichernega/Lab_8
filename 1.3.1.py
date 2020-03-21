# Чернеги Вікторії   Б19_д/122Б
# Програми, що виконують такі операції з масивами:

# 1) виведіть на екран елементи лінійного масиву (заданий користувачем) у зворотньому порядку;

import numpy as np
x = np.array(list(input('Введіть без пробілу: x = ')), dtype = int)            # створення масиву з елементами типу int
print(f'Зворотній порядок {x[::-1]}')                     # вивід елементів масиву за допомогою оператора вилучення зрізу [старт = 1: стоп = довжина масиву: крок = -1]


# 2) виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана користувачем)

a = np.zeros((3,3), dtype = int)                        # створення матриці 3*3, заповненої нулями типу int
for i in range(3):                                      # цикл для проходження по рядкам
    for j in range(3):                                  # цикл для проходження по стовпцям
        a[i,j] = int(input(f'A[{i}, {j}] = '))          # введення елементів матриці
b = np.array(a)                                         # присвоєння даних матриці а матриці b (при транспонуванні будемо використовувати елементи з матриці b)
for i in range(3):                                      # цикл для проходження по рядкам
    for j in range(3):                                  # цикл для проходження по стовпцям
            a [i,j]= b[j,i]                             # заміна елементів матриці а на елементи з матриці b, відносно головної діагоналі
print(f'Транспонована матриця: {a}')                    # вивід транспонованої матриці


# 3) виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність. Результати множення елементів занесіть до нової матриці та виведіть її.

a, b = np.zeros((3,3), dtype = int), np.zeros((3,3), dtype = int)       # створення двох нульових матриць a і b
c, t, summa = [], [], 0                                                 # списки, які будуть використовуватись, та сума елемнетів матриці
for i in range(3):                                                      # цикл для проходження по рядкам матриці а
    for j in range(3):                                                  # цикл для проходження по стовпцям матриці a
        a[i,j] = int(input(f'A[{i}, {j}] = '))                          # введення елементів в матрицю а
for i in range(3):                                                      # цикл для проходження по рядкам матриці b
    for j in range(3):                                                  # цикл для проходження по стовпцям матриці b
        b[i,j] = int(input(f'B[{i}, {j}] = '))
for i in range(3):                                                      # цикл для проходження по рядкам матриці а
    for j in range(3):                                                  # цикл для проходження по стовпцям матриці a
        for z in range(3):                                              # цикл для використання z
            summa += a[i,z] * b[z,j]                                    # сума добутків елементів матриць
            t.append(summa)                                             # занесення кожної суми до списку
        summa = 0                                                       # занулення змінної summa, щоб ек використовувати попередні дані
    c.append(t)                                                         # приєднання списку з сумами до нового списку (створення двовимірного списку)
    t = []                                                              # видалення попередніх сум зі списку для подальшого викоритсання
m = np.array(c)                                                         # перетворення двовимірного списку у масив
print(f'Добуток A*B: {m[::, 2::3]}')                                    # вивід добутку за допомогою зрізу масиву


# 4)у матриці 4*4 замінити всі від'ємні елементи на 0

a = np.zeros((4,4), dtype = int)                                        # створення нульової матриці а
for i in range(4):                                                      # цикл для проходження по рядкам матриці а
    for j in range(4):                                                  # цикл для проходження по стовпцям матриці a
        a[i,j] = int(input(f'A[{i}, {j}] = '))                          # введення елементів до матриці а
for i in range(4):                                                      # цикл для проходження по рядкам матриці а
    for j in range(4):                                                  # цикл для проходження по стовпцям матриці a
        if a[i,j]<0:                                                    # умова: якщо елемент менше 0, то замінити його на нуль
            a[i,j] = 0
print(f"Матриця з нулями замість від'ємних чисел: {a}")                                                                # виведення нової матриці