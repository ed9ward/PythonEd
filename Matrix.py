# Приведение матрицы к красивому виду. Расположение 1 в центре матрицы.
p_of_one = 0
steps = 0
mtr = [[0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]
mid = len(mtr) // 2

for i in range(len(mtr)):
    if 1 in mtr[i] and i < mid:
        mtr[i], mtr[i + 1] = mtr[i + 1], mtr[i]
        steps += 1
        continue
    elif 1 in mtr[i] and i > mid:
        mtr[i], mtr[i - 1] = mtr[i - 1], mtr[i]
        steps += 1
        continue
    elif 1 in mtr[i] and i == mid:
        break

while p_of_one != mid:
    p_of_one = mtr[mid].index(1)
    if p_of_one < mid:
        mtr[mid][p_of_one], mtr[mid][p_of_one + 1] = mtr[mid][p_of_one + 1], mtr[mid][p_of_one]
        steps += 1
    elif p_of_one > mid:
        mtr[mid][p_of_one], mtr[mid][p_of_one - 1] = mtr[mid][p_of_one - 1], mtr[mid][p_of_one]
        steps += 1
    else:
        break

print(*mtr, sep='\n')
print(steps)


# Генерация треугольника Паскаля.
n = int(input('Введите размер матрицы: '))
triangle = []
# Наполняем первые элементы каждого столбца единицами
for i in range(n + 1):
    triangle.append([1] + [0] * n)
# Наполняем список суммой двух элементов над ним. Строки проходим все, но столбцы только до диагонали.
for i in range(1, n + 1):
    for j in range(1, i + 1):
        triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
# Выводим результат
for i in range(0, n + 1):
    for j in range(0, i + 1):
        print(triangle[i][j], end=" ")
    print()


# Сумма каждой из строк и столбцов отдельно. На входе 2 числа - размерность массива, затем - сами списки.
l, c = list(map(int, input().split()))
general = []

for i in range(l):
    general.append(list(map(int, input().split())))

for i in range(l):
    sl = 0
    for j in range(c):
        sl += general[i][j]
    print(sl, end=' ')

print()
for j in range(c):
    sc = 0
    for i in range(l):
        sc += general[i][j]
    print(sc, end=' ')


# Заполнение матрицы n на m змейкой
n, m = list(map(int, input().split()))
g = []
x = 0
for i in range(n):
    g.append([x for x in range(m)])

for i in range(n):
    for j in range(m):
        g[i][j] = x
        x += 1
    if i % 2 != 0:
        g[i].reverse()
    print(g[i])
