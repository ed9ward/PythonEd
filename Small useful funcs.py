# Азбука Морзе
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
inp = list(map(str, input().lower().split()))
for word in inp:
    for l in word:
        print(morze[l], end=' ')
    print()

# Алгоритм Луна для проверки валидности банковской карты.
n = list(input())
new = []
for num, i in enumerate(n):
    if num % 2 == 0:
        if (int(i) * 2) > 9:
            new.append((int(i) * 2) - 9)
        else:
            new.append((int(i) * 2))
    else:
        new.append(int(i))
print(True if sum(new) % 10 == 0 else False)


# Проверка пароля на сложность.
# Сложный пароль имеет длину > 10, больше 3 цифр, одной заглавной буквы и одного спецсимвола.
def check_password(s):
    dig = 0
    upp = 0
    spec = 0

    for l in s:
        if l.isdigit(): dig += 1
        if l.isupper(): upp += 1
        if l in '!@#$%*': spec += 1

    if len(s) < 10 or dig < 3 or upp < 1 or spec < 1: return False
    else: return True

print(check_password('Qwerty171!'))


# Перевод значения цвета из hex в rgb
def from_hex_to_rgb(color: str):
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:], 16)
    return r, g, b


colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A']

for red, green, blue in map(from_hex_to_rgb, colors):
    print(f"Red={red}, Green={green}, Blue={blue}")


# Получение доменного имени сайта
def get_domain_name(url):
    protocol = ('http://www.', 'https://www.', 'http://', 'https://', 'www.')
    for i in range(len(protocol)):
        if protocol[i] in url:
            res = url.replace(protocol[i], '')
            return res.split('.')[0]
    return url.split('.')[0]


get_domain_name("lenovo.com")


# Обход всех файлов и вложенных папок
import os

path = r'D:\@ English'


def scan_dir(my_path, level=1):
    print('Level=', level, 'Content:', os.listdir(my_path))
    for i in os.listdir(my_path):
        if os.path.isdir(my_path + '\\' + i):
            print('Спускаемся', my_path + '\\' + i)
            scan_dir(my_path + '\\' + i, level + 1)
            print('Возвращаемся в', my_path)


scan_dir(path)


# Получение списка папок и файлов.
def get_files(path, depth=0):
    for f in path:
        print(' '*depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth+1)
        else:
            print(' '*(depth+1), ' '.join(path[f]))


F = {'C:': {'Python 3.11': ['py.exe', 'conf.ini']}, 'Program Files': {'Adobe': ['PS.exe'], '7-zip': ['arc.exe']}}
get_files(F)
