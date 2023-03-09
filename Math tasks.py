# Сумма всех четырёхзначных чисел, сумма элементов которых равна 20.
stack = []
for i in range(1000, 10000):
    stack.append(i)
    s = 0
    while i > 0:
        s += i % 10
        i = i // 10
    if s == 20:
        stack.append(i)
        continue
    else:
        stack.pop()
print(sum(stack))


# Проверяет, является ли введённое число степенью 2 и выводит её, или НЕТ.
test = int(input())
i = 1
if test % 2 == 0:
    while 2 ** i < test:
        i += 1
    if test == 2 ** i:
        print(i)
    else: print('НЕТ')
elif test == 1: print(0)
else: print('НЕТ')


# Проверка деления числа на 11.
n = input()
summ, subs = 0, 0
for i in range(len(n)):
    if i % 2 == 0:
        subs += int(n[i])
    else:
        summ += int(n[i])
if subs - summ // 11 == 0:
  ans = 'YES'
else: ans = 'NO'
print(ans)

# Нахождение наименьшего делителя числа, большего 1.
n = int(input())
i = 1
a = []
while i <= n:
    if n % i == 0:
        a.append(i)
    i += 1
print(a[1])

# Считает умножение первой цифры введённого числа на само себя пока первая цифра не станет 1
# или число не станет больше 1млрд
num = int(input())
num1 = int(str(num)[0])
while num1 != 1 and num <= 1000000000:
    num *= num1
    num1 = int(str(num)[0])
    print(num)
print(num)


# Принимает текущее расстояние и цель в км, считает за сколько дней
# можно пройти расстояние, если каждый след день идти на 15% больше.
cur, goal = map(int, input().split())
day = 1
while cur <= goal:
    cur *= 1.15
    day += 1
print(day)


# Разбивает введённое 4х значное число на цифры и выводит их сумму и мультипликацию
num = int(input())
n4 = num % 10
n3 = (num // 10) % 10
n2 = (num // 100) % 10
n1 = num // 1000
print(n1, n2, n3, n4)
print(n1 + n2 + n3 + n4)
print(n1 * n2 * n3 * n4)

# Выводит все комбинации для введённого трёхзначного числа
print(n1, n2, n3, sep='')
print(n1, n3, n2, sep='')
print(n2, n1, n3, sep='')
print(n2, n3, n1, sep='')
print(n3, n2, n1, sep='')
print(n3, n1, n2, sep='')

# Перебирает цифры числа с конца и суммирует их
n = int(input())
summ = 0
while n > 0:
    summ += n % 10
    n = n // 10
print(summ)

# Перебор цифр с конца в поисках мин и макс.
n = int(input())
minn = n % 10
maxx = n % 10
while n > 0:
    if minn > n % 10:
        minn = n % 10
    if maxx < n % 10:
        maxx = n % 10
    n = n // 10
print(minn)
print(maxx)

# Нахождение всех делителей числа. Если мы знаем, что 2 является делителем числа 50, то деля 50 на 2, получаем еще
# один делитель для числа n – это 25. Значит мы можем искать предполагаемый первый делитель
# на интервале от 1 до корня из n (ещё быстрее)
n = int(input())
i = 1
a = []
while i ** 2 <= n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
    i += 1
a.sort()
print(a)

# Алгоритм Евклида для нахождения НОД двух чисел. НОК = a * b / НОК.
a, b = map(int, input().split())
mul = a * b
while b > 0:
    c = a % b
    a = b
    b = c
print('НОД', a)
print('НОК', int(mul / a))
