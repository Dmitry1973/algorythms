# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

num = ''
HEX_CYPHER = ['A', 'B', 'C', 'D', 'E', 'F',
              '0', '1', '2', '3', '4', '5',
              '6', '7', '8', '9', ]
hex_numbers = []
counter = 1

while True:
    if num == ['Q']:
        break

    while counter < 3:
        print(f'введите {counter}- ое шестнадцатеричное число или q для выхода')
        num = list(input('num ').upper())
        res = [n for n in num if n in HEX_CYPHER]
        if num == ['Q']:
            break
        elif num != res:
            print('not hex entered')
        else:
            hex_numbers.append(num)
            counter += 1

    break

if hex_numbers:
    num1 = int(str([''.join(hex_numbers[0])][0]), 16)
    num2 = int(str([''.join(hex_numbers[1])][0]), 16)

    print(f'{hex(num1)}, {hex(num2)}')
    action = input('enter operation "+" or "*" or "m"')  # при вводе m - и складывает и умножет
    if action == '+':
        print(f'{hex(num1)} + {hex(num2)} = {hex(num1 + num2)}')
    elif action == '*':
        print(f'{hex(num1)} * {hex(num2)} = {hex(num1 * num2)}')
    elif action == 'm':
        print(f'{hex(num1)} + {hex(num2)} = {hex(num1 + num2)}')
        print(f'{hex(num1)} * {hex(num2)} = {hex(num1 * num2)}')
    else:
        pass
