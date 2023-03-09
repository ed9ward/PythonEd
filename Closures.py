# Увеличивает значение на переданное число.
def adder():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner


first = adder()
second = adder()
print(first(2))
print(first(3))
print(second(10))
print(second(9))
print('_____')


# Возведение в степень с помощью замыкания и лямбда функции.
def power(base):
    return lambda value: value ** base


a = power(2)
b = power(10)
print(a(5))
print(b(5))
print('_____')


# Создание словаря с добавлением значений.
def create_dict():
    my_dict = {}
    count = 1

    def inner(s):
        nonlocal my_dict, count
        my_dict[count] = s
        count += 1
        return my_dict

    return inner


a = create_dict()
print(a('First'))
print(a('Second'))
print(a('Third'))
print('_____')


# Вывод типов принятых функцией аргументов.
def print_given(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))
    for kwarg in kwargs:
        print(kwarg, type(kwargs[kwarg]))


print_given(1, [1, 2, 3], 'one', one=1, three=(1, 2))
print('_____')


# Счётчик уменьшается на 1 при каждом вызове.
def countdown(n):
    def step():
        nonlocal n
        r = n
        n -= 1
        return r

    return step


do_step = countdown(10)
print(do_step())
print(do_step())
print('_____')


# Позднее замыкание. Считывание данных и их заморозка происходит в момент вызова,
# и в первом примере у нас останется только последний элемент списка в замыкании.
def wrong_set_names(names):
    results = []
    for name in names:
        def inner(surname):
            return name + ' ' + surname

        results.append(inner)
    return results


def set_names(names):
    results = []
    for name in names:
        def inner(surname, name=name):
            return name + ' ' + surname

        results.append(inner)
    return results


names_lst = ['Roy', 'Jake', 'Colin']
for child_name in wrong_set_names(names_lst):
    print(child_name('Robinson'))
for child_name in set_names(names_lst):
    print(child_name('Robinson'))
print('_____')


# Использование функции как обьекта.
def func_as_object(a, b):
    def add():
        return a + b

    def sub():
        return a - b

    def mul():
        return a * b

    def replace():
        pass

    replace.add = add
    replace.sub = sub
    replace.mul = mul
    return replace


ex1 = func_as_object(2, 5)
ex2 = func_as_object(5, 10)
print(ex1.add())
print(ex2.mul())
