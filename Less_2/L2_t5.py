# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

print('-' * 101)
for i in range(32, 128):
    if i < 100:
        m = ' ' + str(i)
        print('|', m, '->', chr(i), end='')
        if (i - 1) % 10 == 0 or i == 127:
            print('|')
            print('-' * 101)
    else:
        print('|', i, '->', chr(i), end='')
        if (i - 1) % 10 == 0 or i == 127:
            print('|')
            if i < 127:
                print('-' * 101)
            else:
                print('-' * 61)
