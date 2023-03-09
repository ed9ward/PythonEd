# Считает самую часто встречаемую ввудённую букву в любом регистре
l = input()
maxs = 0
for i in range(len(l)):
    if maxs < l.lower().count(l[i].lower()):
        maxs = l.lower().count(l[i].lower())
print(maxs)


# Выводит все непустые строки пронумерованными с 1.
def print_goods(*args):
    n = 1
    for i in args:
        if isinstance(i, str) and i not in ('', ' '):
            print(n, '.', i)
            n += 1
    if n == 1: print('Нет товаров')


print_goods(1, True, ' ', 'Tomatoes')


# Проверяем каждую букву, являются ли они 'a'или 'e' и выводим все остальные.
strn = input()
i = 0

while i < len(strn):
    if strn[i] in ('a', 'e'):
        print('Ага! Нашлась')
        break
    else:
        print(f'Текущая буква: {strn[i]}')
        i += 1
else:
    print('Распечатали все буквы')

# Найдите, в каких строках из введённых и в каком месте упоминается "рок", причем регистр букв не важен.
# На первой строке вводится натуральное число N — количество строк. Далее следуют N строк.
strings = []
n = int(input())
for i in range(n):
    strings.append(input())
    if 'рок' in strings[i].lower():
        print(i+1, strings[i].lower().index('рок') + 1)


# Переворачивает часть строки между первым и вторым h
s = input()
fi = 0
si = 0
for l in s:
    if l == 'h':
        fi = s.index(l)
        si = s.find('h', fi+1)
        break
sl = s[:fi] + s[si:fi:-1] + s[si:]
print(sl)


# Превращает вложенные списки в простой линейный список.
def flatten(l):
    s = []
    if len(l) == 0:
        return s
    for i in l:
        if isinstance(i, list): s += flatten(i)
        else: s.append(i)
    return s


flatten([1, [2, 3, [4]], 5])


# Принимает на ввод через пробел данные, выводит все числа в список,
# текст для не числовых данных и после пустого ввода подсчитывает минимальное число в списке.
nums = []
i = 0

while 1:
    numbr = list(map(str, input().split()))
    for i in range(len(numbr)):
        print('Работаем с:', numbr[i])
        if numbr[i].isdecimal():
            nums.append(int(numbr[i]))
            print('Список выглядит так:', nums)
        else:
            print('Not a number !')
        i += 1
    if len(numbr) == 0:
        break

print('Минимальное число:', min(nums))


# В вашем распоряжении имеется два отсортированных списка по не убыванию элементов, состоящих из n и m элементов
# Ваша задача слить их в один отсортированный список размером n + m
# Входные данные: Программа получает на вход два числа n и m - количество элементов первого списка и второго списков
# Затем с новой строки поступают элементы первого отсортированного списка, а со следующей строки - второго списка
# Выходные данные: Слить два списка в один в порядке не убывания и вывести элементы полученного списка

_, l1, l2 = input(), list(map(int, input().split())), list(map(int, input().split()))
l_join = list(l1 + l2)
res = []
while len(l_join) > 0:
    res.append(l_join.pop(l_join.index(min(l_join))))
print(*res)
