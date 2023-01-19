import random


def validation_symbol():
    flag = True
    while flag:
        symbol = input()
        if not symbol.isdigit():
            print('Введите цифру:')
            continue
        else:
            return int(symbol)


def validation_char():
    flag = True
    while flag:
        char = input()
        if char not in 'yn':
            print('Введите y или n:')
            continue
        elif char == 'y':
            return 1
        else:
            return 0


def password_generate(p_n, p_l, p_d, p_u_c, p_l_c, p_s, p_s_s):
    digits = '0123456789'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''
    if p_d == 1:
        chars += digits
    if p_u_c == 1:
        chars += uppercase_letters
    if p_l_c == 1:
        chars += lowercase_letters
    if p_s == 1:
        chars += punctuation
    chars = [c for c in chars]
    password = []
    if p_s_s == 1:
        if p_d == 1:
            chars.remove('0')
            chars.remove('1')
        if p_u_c == 1:
            chars.remove('I')
            chars.remove('L')
            chars.remove('O')
        if p_l_c == 1:
            chars.remove('i')
            chars.remove('l')
            chars.remove('o')
    for i in range(p_n):
        pass_temp = []
        for j in range(p_l):
            pass_temp.append(random.choice(chars))
        password.append(''.join(pass_temp))
    return password


print('Добро пожаловать в генератор паролей')

print('Укажите количество паролей для генерации:')
pass_num = validation_symbol()
print('Укажите длину одного пароля:')
pass_len = validation_symbol()
print('Включить в пароль цифры 0123456789? y/n')
pass_dig = validation_char()
print('Включить в пароль прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? y/n')
pass_up_case = validation_char()
print('Включить в пароль строчные буквы abcdefghijklmnopqrstuvwxyz? y/n')
pass_low_case = validation_char()
print('Включить в пароль символы !#$%&*+-=?@^_? y/n')
pass_sym = validation_char()
print('Исключить из пароля похожие символы iI1lLoO0? y/n')
pass_s_sym = validation_char()

print(*password_generate(pass_num, pass_len, pass_dig, pass_up_case, pass_low_case, pass_sym, pass_s_sym), sep='\n')
