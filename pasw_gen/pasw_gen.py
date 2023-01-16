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


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation =  '!#$%&*+-=?@^_'
chars = ''
print('Добро пожаловать в генератор паролей')
print('Укажите количество паролей для генерации:')
password_number = validation_symbol()
print('Укажите длину одного пароля:')
password_lenght = validation_symbol()
print('Включать ли цифры 0123456789? y/n')
password_digit = validation_char()
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? y/n')
password_upper_case = validation_char()
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? y/n')
password_lower_case = validation_char()
print('Включать ли символы !#$%&*+-=?@^_? y/n')
password_symbols = validation_char()
print('Исключать ли неоднозначные символы il1Lo0O? y/n')
password_similar_symbols = validation_char()

