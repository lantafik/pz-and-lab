from back import *

a, b, c = map(float, input('Введите коэффициенты a, b, c ').split())

d = get_math_text(a, b, c)
n = len(d)

if d[0] == None:
    print('Не удалось посчитать дискриминант')
elif n == 1:
    print(f"x1 = {d[0]}")
else:
    print(f"x1 = {d[0]}\nx2 = {d[1]}")

