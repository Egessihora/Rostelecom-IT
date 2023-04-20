from faker import Faker
import string

base_url = "https://b2c.passport.rt.ru"
"""Базовый URL тестируемого сайта РосТелеКом"""

# Валидные данные:
valid_email = "n14yoencs@qiott.com"
valid_password = 'No!3V75d#q'
valid_firstname = "Анастасия"
valid_lastname = "Ягужинская"
valid_login = "Egessa"
valid_region = "Москва"

# Невалидные данные:
random = Faker()

# Случайный пароль:
random_password = random.password()
# Случайный адрес электронной почты:
random_email = random.email()

invalid_ls = "269750005232"
invalid_login = "test_login"
invalid_phone = "+79211234567"


def generate_string_rus(n):
    return 'я' * n   # генерация строки из букв на кириллице


def generate_string_en(n):
    return "s" * n   # генерация строки из букв на латинице


def english_chars():
    return 'qwertyuiopasdfghjklzxcvbnm'   # английский алфавит


def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'   # русский алфавит


def special_chars():
    return f'{string.punctuation}'  # специальные симовлы


def japanese_symbols():  # популярные японские иероглифы
    return '原千五百秋瑞'


def chinese_symbols():  # популярные китайсике иероглифы
    return '龍門大酒家'
