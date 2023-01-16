import random


def validation_symbol():
    flag = True
    while flag:
        symbol = input()
        if symbol not in '1234567890':
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
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''
    if p_d == 1:
        chars += digits
    if p_u_c == 1:
        chars += lowercase_letters
    if p_l_c == 1:
        chars += uppercase_letters
    if p_s == 1:
        chars += punctuation


print('Добро пожаловать в генератор паролей')

print('Укажите количество паролей для генерации:')
pass_number = validation_symbol()
print('Укажите длину одного пароля:')
pass_lenght = validation_symbol()
print('Включить в пороль цифры 0123456789? y/n')
pass_digit = validation_char()
print('Включить в пароль прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? y/n')
pass_upper_case = validation_char()
print('Включить в пароль строчные буквы abcdefghijklmnopqrstuvwxyz? y/n')
pass_lower_case = validation_char()
print('Включить в пароль символы !#$%&*+-=?@^_? y/n')
pass_symbols = validation_char()
print('Исключить из пароля похожие символы iI1lLoO0? y/n')
pass_similar_symbols = validation_char()

password_generate(pass_number, pass_lenght, pass_digit, pass_upper_case, pass_lower_case, pass_symbols, pass_symbols)





