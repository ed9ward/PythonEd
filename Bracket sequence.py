# Проверка на правильную скобочную последовательность
s = input()
sl = [x for x in s]
x = 0
for i in range(len(sl)):
    if sl[i] == '(':
        x += 1
    else:
        x -= 1
        if x < 0:
            break
print('YES' if x % 2 == 0 else 'NO')

# Проверка на правильную скобочную последовательность с разными скобками
s = input()
stack = []
valid = True
for i in s:
    if i in '([{':
        stack.append(i)
    elif i in ')]}':
        if not stack:
            valid = False
            break
        opened = stack.pop()
        if opened == '(' and i == ')': continue
        if opened == '[' and i == ']': continue
        if opened == '{' and i == '}': continue
        else:
            valid = False
            break
print('YES' if valid and len(stack) == 0 else 'NO')

# Проверка на правильную скобочную последовательность с разными скобками v 2.0
s = input()
stack, openers, closers = [], [], []
valid = True
tup = (('(', ')'), ('{', '}'), ('[', ']'), ('\\', '/'), ('d', 'b'))

for i in range(len(tup)):
    openers.append(tup[i][0])
for i in range(len(tup)):
    closers.append(tup[i][1])

for i in s:
    if i in openers:
        stack.append(i)
    elif i in closers:
        if not stack:
            valid = False
            break
        opened = stack.pop()
        valid = False
        for e in range(len(tup)):
            if opened in tup[e] and i in tup[e]:
                valid = True
                break
        if not valid: break

print('YES' if valid and len(stack) == 0 else 'NO')
