""" Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""


def func(num):
    even = 0
    odd = 0
    for f in str(num):
        if int(f) % 2 == 0:
            even += 1
        else:
            odd += 1
    return f'В вашем числе {even} четных цифр и {odd} нечетных'


print(func(722))
