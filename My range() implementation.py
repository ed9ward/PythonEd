# My implementation of built-in function range() with generator.
# Works the same way - three parameters: start, stop, step.

def my_range_gen(fir, sec=None, thr=None):
    if sec is None:
        start = 0
        stop = fir
        step = 1
    elif thr is None:
        start = fir
        stop = sec
        step = 1
    elif thr == 0:
        print("Step can't be zero")
    else:
        start = fir
        stop = sec
        step = thr

    if step > 0:
        while start < stop:
            yield start
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step


for i in my_range_gen(30, 40, 1): print(i)


# Generators
def gen_squares(i):
    for sq in range(1, i + 1):
        yield sq ** 2


for i in gen_squares(4): print(i)


# Fibonacci numbers with generator
def gen_fibonacci_numbers(i):
    a, b = 1, 1
    for fib in range(i):
        yield a
        a, b = b, a + b


for i in gen_fibonacci_numbers(30): print(i)

# Pattern printer generator
pat = ['(', '{', '[', ']', '}', ')']


def cur_pattern(sample):
    i = 0
    while True:
        if i >= len(sample):
            i = 0
        yield sample[i]
        i += 1


ptt = cur_pattern(pat)
for i in range(10): print(next(ptt))
