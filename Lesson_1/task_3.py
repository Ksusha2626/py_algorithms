"""Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв."""

res = None
x, y = input('Введите две любые маленькие буквы английского алфавита через пробел: ').split()

x = ord(x) - ord('a') + 1
y = ord(y) - ord('a') + 1
if x < y:
    res = (y - x) - 1
elif x > y:
    res = (x - y) - 1
else:
    res = 0

print(f'Между введенными буквами находится {res} букв')