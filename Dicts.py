# Dictionary structure reformation.
import timeit
import copy

persons = [('Allison Hill', 334053, 'M', '1635644202'),
           ('Megan Mcclain', 191161, 'F', '2101101595'),
           ('Brandon Hall', 731262, 'M', '6054749119'),
           ('Michelle Miles', 539898, 'M', '1355368461'),
           ('Donald Booth', 895667, 'M', '7736670978'),
           ('Gina Moore', 900581, 'F', '7018476624'),
           ('James Howard', 460663, 'F', '5461900982'),
           ('Monica Herrera', 496922, 'M', '2955495768'),
           ('Sandra Montgomery', 479201, 'M', '5111859731'),
           ('Amber Perez', 403445, 'M', '0602870126')]


def person_data_unpack():
    data = {}
    for pers in persons:
        perdata = {}
        perdata['salary'] = pers[1]
        perdata['gender'] = pers[2]
        perdata['passport'] = pers[3]
        data[pers[0]] = perdata
        # data[pers[0]] = copy.copy(perdata)
        # data[pers[0]] = dict(perdata)
        # data[pers[0]] = perdata.copy()
    return data


print(timeit.timeit('person_data_unpack()', globals=globals()))
print(person_data_unpack())

# Simple registration DB imitation. Saves user if name is unique, add number in the end if not.
# Input: Number of users. Then Name of the user.
db = {}
n = int(input())
for i in range(n):
    req = input()
    if req not in db:
        db[req] = 'user'
        print('OK')
    else:
        for c in range(1, 10):
            if db.get(req + str(c)) is not None:
                continue
            else:
                print(db.setdefault(req + str(c), req + str(c)))
                break


# Nested dict flattening.
nes = {'Germany': {'berlin': {'now': 7}}, 'Europe': {'italy': {'Rome': 3}}, 'USA': {'washington': 1, 'New York': 4}}


def flatten_dict(d: dict) -> dict:
    res = {}
    for kp, vp in d.items():
        res.update({f'{kp}_{k}': v for k, v in flatten_dict(vp).items()} if type(vp) is dict else {kp: vp})
    return res


print(flatten_dict(nes))


# Counts the number of symbols in string. Not case-sensitive.
def symbol_counter(inp: str):
    inp = input()
    d = {}
    for symb in inp:
        if symb.lower().isalpha():
            d[symb.lower()] = d.get(symb.lower(), 0) + 1
    return d


# Выводит ключ = значение отсортированные по алфавиту
def foo(**kwargs):
    print(*[f'{k} = {v}' for k, v in sorted(kwargs.items())], sep='\n')


foo(first_name="John", last_name="Doe", age=33)

# Принимает кол-во вводов, телефон и имя, потом кол-во запросов и выводит телефоны по запросу имени
'''3
444444 Женя
79129874521 Женя
79604845827 Оля
3
Оля
Олег
Женя'''

d = {}
for i in range(int(input())):
    a, b = input().split()
    if b not in d:
        d[b] = [a]
    else:
        d[b].append(a)

for i in range(int(input())):
    q = input()
    if q in d.keys():
        print(*d[q])
    else: print('Неизвестный номер')

# Считывает набор имён и оценок до ввода слова конец. Выводит имя и среднюю оценку в порядке убывания.
'''Input: 
First, 1, 3, 4, 5
Second, 1, 2, 3, 5 
конец'''
taxists = {}

while True:
    c = input().split(', ')
    if c[0] == 'конец': break

    if c[0] not in taxists:
        taxists[c[0]] = [int(c[1])]
    else:
        taxists[c[0]].append(int(c[1]))

for k, v in sorted(taxists.items(), key=lambda x: (-sum(x[1]) / len(x[1]), x[0])):
    print(k, (sum(taxists[k]) / len(taxists[k])))


# Выводит макс и мин упоминаемого актёра
'''6
Леонардо Ди Каприо
Джонни Депп
Леонардо Ди Каприо
Леонардо Ди Каприо
Джонни Депп
Мэтт Деймон'''

x = int(input())
d = {}
for i in range(x):
    act = input()
    if act not in d:
        d[act] = 1
    else:
        d[act] += 1

print(*max(d.items(), key=lambda x: x[1]), sep=', ')
print(*min(d.items(), key=lambda x: x[1]), sep=', ')
print(sorted(d, key=lambda x: d[x], reverse=True))


# Считывает кол-во вводов, принимает имя, день, месяц рождения.
# Потом кол-во выводов и выводит имена тех, кто родился в этом мес.
'''4
Саша 20 янв
Артем 15 июн
Карл 10 янв
Коля 20 июл
3
июн
дек
янв'''

d = {}
mounth_names = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
mnths = {k: v for v, k in enumerate(mounth_names, 1)}
print(mnths)

for i in range(int(input())):
    a, b, c = input().split()
    mnth_num = mnths[c]
    d[a] = (b, c, mnth_num)

print(d)
b = sorted(d, key=lambda x: (d[x][2], d[x][0]))
print(b)

for i in range(int(input())):
    q = input()
    flag = False
    for k, v in d.items():
        if v[1] == q:
            print(k)
            flag = True
    if not flag: print('Нет данных')
