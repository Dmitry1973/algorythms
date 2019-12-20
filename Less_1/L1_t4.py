# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

alpha3 = ord(input('введите первый латинский символ '))
alpha4 = ord(input('введите второй латинский символ '))

# смещение символа "а"
shift = ord('a') - 1
place1 = alpha3 - shift
place2 = alpha4 - shift

if place1 == place2 or abs(place1 - place2) == 1:
    ltr = 0
else:
    ltr = abs(place1 - place2) - 1

print(f'"{chr(alpha3)}" на {place1} месте в алфавите, "{chr(alpha4)}" на {place2},\nбукв между ними {ltr}')
