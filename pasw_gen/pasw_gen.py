import random

def validation_symbol(symbol):
    if symbol not in 1234567890:
        print('Введите цифру:')
def validation_char(char):
    if char not in 'y' or 'n':
        print('Введите правильный символ:')



digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation =  '!#$%&*+-=?@^_'
chars = ''

print('Добро пожаловать в генератор паролей')
print('Укажите длину одного пароля:')
password_lenght = int(input())
validation_symbol(password_lenght)
print('Включать ли цифры 0123456789? y/n')
password_digit = input()
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? y/n')
password_upper_case = input()
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? y/n')
password_lower_case = input()
print('Включать ли символы !#$%&*+-=?@^_? y/n')
password_symbols = input()
print('Исключать ли неоднозначные символы il1Lo0O? y/n')
password_similar_symbols = input()


