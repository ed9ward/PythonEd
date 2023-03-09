from functools import wraps
from time import time


# Первый декоратор.
def text_decor(func):
    def wrap(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye!')

    return wrap


@text_decor
def multiply(num1, num2):
    print(num1 * num2)


multiply(3, 5)
print('_____')


# Проверяет, что первый аргумент будет равен определённому значению.
def check_if_first_arg_is(value):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                print(f'First argument has to be {value}')
            return func(*args, **kwargs)

        return wrapper

    return inner_dec


@check_if_first_arg_is('red')
def print_rainbow_colors(*colors):
    print(colors)


@check_if_first_arg_is(7)
def multiply_7(a, b):
    return a * b


print_rainbow_colors('orange', 'yellow', 'green', 'blue',
                     'indigo', 'violet')
print(multiply_7(7, 3))
print(multiply_7(6, 3))
print('_____')


# Насильно приводит аргументы к определённым типам
def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return func(*new_args, **kwargs)

        return wrapper

    return inner_dec


@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)


@enforce(float, float)
def divide(a, b):
    return a / b


print_text_n_times('Hi!', '3')
print(divide(4, 2))
print(divide('4', '2'))
print('_____')


# Замер скорости выполнения функции
def speed_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time of code execution {end_time - start_time}")
        return result

    return wrapper


@speed_test
def sum_with_list():
    return sum([number for number in range(10000000)])


@speed_test
def sum_with_gen():
    return sum(number for number in range(10000000))


print(sum_with_list())
print(sum_with_gen())
