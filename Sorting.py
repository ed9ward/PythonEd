# Метод сортировки подсчётом. На входе числа от -100 до 100.
# Input: 5 6 89 1
# Output: 1 5 6 89
def count_sort():
    n = list(map(int, input().split()))
    lst = [0] * 201
    for i in n:
        lst[i + 100] += 1
    for i in range(201):
        if lst[i] > 0:
            print((str(i - 100) + ' ') * lst[i], end='')
    return lst


# Сортировка сравнением.
# Input: 2 56 8 1 1 2 98
# Output: 1 1 2 2 8 56 98
def compare_sort():
    lst = list(map(int, input().split()))
    cur = 0
    for x in range(1, len(lst)):
        cur = lst.pop(x)
        for i in range(1, x + 1):
            if cur < lst[x - i]:
                if x - i == 0:
                    lst.insert(x - i, cur)
                continue
            else:
                lst.insert(x - i + 1, cur)
                break
    return lst


# Пузырьковая сортировка с выводом кол-ва перестановок.
# Input: 2 0 45 5 89 2
# Output: 0 2 2 5 45 89
# 5 перестановок
def bubble_sort():
    lst = list(map(int, input().split()))
    count = 0
    for x in range(len(lst) - 1):
        for i in range(len(lst) - x):
            for j in range(i + 1, len(lst) - x):
                if lst[j] < lst[i]:
                    lst[i], lst[j] = lst[j], lst[i]
                    count += 1
                    break
                elif lst[j] >= lst[i]:
                    break
    print(f'{count} перестановок')
    return lst


# Быстрая сортировка Хоара через рекурсию.
# Input: [9, 5, -3, 4, 7, 8, -8]
# Output: [-8, -3, 4, 5, 7, 8, 9]
def quick_sort(lst):
    import random
    if len(lst) > 1:
        x = random.choice(lst)
        low = [u for u in lst if u < x]
        eq = [u for u in lst if u == x]
        hi = [u for u in lst if u > x]
        lst = quick_sort(low) + eq + quick_sort(hi)
    return lst


# Сортировка слиянием через рекурсию.
# Input: [6, 2, 19, 5, 10, 7, 11]
# Output: [2, 5, 6, 7, 10, 11, 19]
def merge_two_list(a, b):
    i = 0
    j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged += a[i:] + b[j:]
    return merged


def merge_sort(s):
    mid = len(s) // 2
    l = s[:mid]
    r = s[mid:]
    if len(l) > 1:
        l = merge_sort(l)
    if len(r) > 1:
        r = merge_sort(r)
    return merge_two_list(l, r)


# Sorting with progress bar
from random import randint
from tqdm import trange, tqdm
from time import sleep

lst = []
for i in range(100):
    lst.append(randint(0, 999))


def sort_ed(lst):
    cur = 0
    for x in trange(1, len(lst)):
        sleep(0.01)
        cur = lst.pop(x)
        for i in range(1, x + 1):
            if cur < lst[x - i]:
                if x - i == 0:
                    lst.insert(x - i, cur)
                continue
            else:
                lst.insert(x - i + 1, cur)
                break
    print()
    return lst


print(sort_ed(lst))
