# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


def is_hex_number(check_num: str) -> (list, int):
    """Get as input string, check the input string and return
    list separated hex cyphers and
    int representation"""

    hex_number = []
    check_num = list(check_num.upper())
    hex_cypher = ['A', 'B', 'C', 'D', 'E', 'F',
                  '0', '1', '2', '3', '4', '5',
                  '6', '7', '8', '9', ]
    res = [n for n in check_num if n in hex_cypher]

    if check_num != res or check_num == []:
        return False
    else:
        hex_number.append(check_num)
        num = int(str([''.join(hex_number[0])][0]), 16)

    return hex_number, num


def hex_math(num1: int, num2: int, operation=''):
    """Get two int numbers and depending on operation type:
    -- if "+" return num1 + num2
    -- if "*" return num1 * num2
    -- if any return both - this is default setting"""

    if operation == '*':
        return print(f'product of {hex(num1)} and {hex(num2)} is {hex(num1 * num2)}'
                     f'\n{list((hex(num1 * num2)).upper())[2:]}')

    elif operation == '+':
        return print(f'sum of {hex(num1)} and {hex(num2)} is {hex(num1 + num2)}'
                     f'\n{list((hex(num1 + num2)).upper())[2:]}')

    else:
        return print(f'product:\n \b{hex(num1)} * {hex(num2)} = {hex(num1 * num2)}''\n' 
                     f'{list((hex(num1 * num2)).upper())[2:]}''\n' 
                     f'{"-"*30}'                                                                                   
                     f'\nsum:\n \b{hex(num1)} + {hex(num2)} = {hex(num1 + num2)}''\n'
                     f'{list((hex(num1 + num2)).upper())[2:]}''\n'
                     f'{"-"*30}')


def main():
    """Запускает все это безобразие
    launched all this ...
    """

    while True:
        to_continue = input('q - for exit, any to continue ')
        if to_continue == 'q':
            break
        else:
            hex_num1 = is_hex_number(input('please 1st enter hex number '))
            if not hex_num1:
                print('please enter correct hex number!')
            else:
                hex_num2 = is_hex_number(input('please 2nd enter hex number '))
                if not hex_num2:
                    print('please enter correct hex number!')
                else:
                    # action = input('please enter operation "+", "*" ')
                    print('-'*30)
                    print(*hex_num1[0])
                    print(*hex_num2[0])
                    print('-' * 30)
                    hex_math(hex_num1[1], hex_num2[1],)  # action)
    return None


main()
