import pytest
from pages.RosTeleCom_APP import *
from pages.settings import *
import time


# RTC-032
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize("firstname", ["", generate_string_rus(1), generate_string_rus(31),
                                       generate_string_rus(256), english_chars(),
                                       special_chars(), 78489, japanese_symbols(),
                                       chinese_symbols()],
                         ids=['RTC-032-1) empty line', 'RTC-032-2) one char', 'RTC-032-3) 31 chars',
                              'RTC-032-4) 256 chars', 'RTC-032-5) english', 'RTC-032-6) special',
                              'RTC-032-7) number', 'RTC-032-8) japanese_symbols', 'RTC-032-9) chinese_symbols'])
def test_get_registration_invalid_format_firstname(browser, firstname):
    page = AuthPage(browser)
    page.enter_reg_page()  # нажимаем на кнопку "Зарегистрироваться"
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)
    page.enter_firstname(firstname)  # вводим невалидное имя
    browser.implicitly_wait(2)

    page.enter_lastname(valid_lastname)  # вводим валидную фамилию
    browser.implicitly_wait(2)

    page.enter_email(valid_email)  # вводим валидный адрес адрес электронной почты
    browser.implicitly_wait(2)

    page.enter_password(valid_password)  # вводим валидый пароль
    browser.implicitly_wait(2)

    page.enter_pass_conf(valid_password)  # вводим валидное подтверждение пароля
    browser.implicitly_wait(2)

    page.btn_click()  # нажимаем на кнопку "Зарегистрироваться"
    error_mess = browser.find_element(*AuthLocators.AUTH_MESSAGE_ERROR)

    assert error_mess.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    print(f"RTC-032-(1-9)"
          f"\nНегативный сценарий регистрации в личном кабинете РосТелеКом: "
          f"невалидый формат Имени.")
    print('Сообщение об ошибке: "Необходимо заполнить поле кириллицей. От 2 до 30 символов."')


# RTC-033
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize("lastname", ["", generate_string_rus(1), generate_string_rus(31),
                                      generate_string_rus(256), english_chars(),
                                      special_chars(), 78489, japanese_symbols(),
                                      chinese_symbols()],
                         ids=['RTC-033-1) empty line', 'RTC-033-2) one char', 'RTC-033-3) 31 chars',
                              'RTC-033-4) 256 chars', 'RTC-033-5) english', 'RTC-033-6) special',
                              'RTC-033-7) number', 'RTC-033-8) japanese_symbols', 'RTC-033-9) chinese_symbols'])
def test_get_registration_invalid_format_lastname(browser, lastname):
    page = AuthPage(browser)
    page.enter_reg_page()  # нажимаем на кнопку "Зарегистрироваться"
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)

    page.enter_firstname(valid_firstname)  # вводим валидное имя
    browser.implicitly_wait(5)

    page.enter_lastname(lastname)  # вводим невалидную фамилию
    browser.implicitly_wait(5)

    page.enter_email(valid_email)  # вводим валидный адрес электронной почты
    browser.implicitly_wait(3)

    page.enter_password(valid_password)  # вводим валидный пароль
    browser.implicitly_wait(3)

    page.enter_pass_conf(valid_password)  # вводим валидное подтверждение пароля
    browser.implicitly_wait(3)

    page.btn_click()  # нажимаем на кнопку "Зарегистрироваться"
    error_mess = browser.find_element(*AuthLocators.AUTH_MESSAGE_ERROR)

    assert error_mess.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    print(f"RTC-033-(1-9)"
          f"\nНегативный сценарий регистрации в личном кабинете РосТелеКом: "
          f"невалидый формат Фамилии.")
    print('Сообщение об ошибке: "Необходимо заполнить поле кириллицей. От 2 до 30 символов."')


# RTC-034
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize("phone", ["", 1, 1111111111, generate_string_rus(11), english_chars(), special_chars()],
                         ids=['RTC-034-1) empty line', 'RTC-034-2) one digit', 'RTC-034-3) 10_digits',
                              'RTC-034-4) string_rus', 'RTC-034-5) english_chars', 'RTC-034-6) special_chars'])
def test_get_registration_invalid_format_phone(browser, phone):
    page = AuthPage(browser)
    page.enter_reg_page()  # нажимаем на кнопку "Зарегистрироваться"
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)

    page.enter_firstname(valid_firstname)  # вводим валидное имя
    browser.implicitly_wait(5)

    page.enter_lastname(valid_lastname)  # вводим валидную фамилию
    browser.implicitly_wait(5)

    page.enter_email(phone)  # вводим невалидный номер мобильного телефона
    browser.implicitly_wait(3)

    page.enter_password(valid_password)  # вводим валидный пароль
    browser.implicitly_wait(3)

    page.enter_pass_conf(valid_password)  # вводим валидное подтверждение пароля
    browser.implicitly_wait(3)

    page.btn_click()  # нажимаем на кнопку "Зарегистрироваться"

    error_mess = browser.find_element(*AuthLocators.AUTH_MESSAGE_ERROR)
    assert error_mess.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, " \
                              "или email в формате example@email.ru"
    print(f"RTC-034-(1-6)"
          f"\nНегативный сценарий регистрации в личном кабинете РосТелеКом: "
          f"невалидый формат номера телефона."
          "\nПрименена техника анализа классов эквивалентности.")
    print('Сообщение об ошибке: "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, '
          'или email в формате example@email.ru"')


# RTC-035
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize("email", ["", "@", "@.", ".", generate_string_rus(20),
                                   f"{russian_chars()}@mail.ru", 77777],
                         ids=['RTC-035-1) empty line', 'RTC-035-2) at', 'RTC-035-3) at point',
                              'TRK-035-4) point', 'RTC-035-5) string', 'RTC-035-6) russian',
                              'RTC-035-7) digits'])
def test_get_registration_invalid_format_email(browser, email):
    page = AuthPage(browser)
    page.enter_reg_page()   # нажимаем на кнопку "Зарегистрироваться"
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)
    page.enter_firstname(valid_firstname)   # вводим валидное имя
    browser.implicitly_wait(5)

    page.enter_lastname(valid_lastname)   # вводим валидную фамилию
    browser.implicitly_wait(5)

    page.enter_email(email)   # вводим невалидный адрес электронный почты
    browser.implicitly_wait(3)

    page.enter_password(valid_password)   # вводим валидный пароль
    browser.implicitly_wait(3)

    page.enter_pass_conf(valid_password)   # вводим валидное подтверждение пароля
    browser.implicitly_wait(3)

    page.btn_click()   # нажимаем на кнопку "Зарегистрироваться"
    error_mess = browser.find_element(*AuthLocators.AUTH_MESSAGE_ERROR)

    assert error_mess.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, " \
                              "или email в формате example@email.ru"
    print(f"RTC-035-(1-7)"
          f"\nНегативный сценарий регистрации в личном кабинете РосТелеКом: "
          f"невалидый формат адреса электронной почты.")
    print('Сообщение об ошибке: "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, '
          'или email в формате example@email.ru"')


# RTC-036
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize("living_email", [valid_email], ids=["living email"])
def test_get_registration_living_account(browser, living_email):
    page = AuthPage(browser)
    page.enter_reg_page()   # нажимаем на кнопку "Зарегистрироваться"
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)
    page.enter_firstname(valid_firstname)   # вводим валидное имя
    browser.implicitly_wait(5)

    page.enter_lastname(valid_lastname)   # вводим валидную фамилию
    browser.implicitly_wait(5)

    page.enter_email(living_email)   # вводим зарегистрированный в системе адрес электронной почты
    browser.implicitly_wait(3)

    page.enter_password(valid_password)   # вводим валидный пароль
    browser.implicitly_wait(3)

    page.enter_pass_conf(valid_password)   # вводим валидное подтверждение пароля
    browser.implicitly_wait(3)

    page.btn_click()   # нажимаем на кнопку "Зарегистрироваться"
    time.sleep(2)
    card_modal_title = browser.find_element(*RegLocators.REG_CARD_MODAL)

    assert card_modal_title.text == "Учётная запись уже существует"
    print(f"RTC-036"
          f"\nНегативный сценарий регистрации в личном кабинете РосТелеКом: "
          f"зарегистрированный в системе адрес электронной почты.")
    print('Сообщение об ошибке: "Учётная запись уже существует"')


# RTC-037
@pytest.mark.reg
@pytest.mark.negatvie
def test_get_registration_pass_diff_pass_conf(browser):
    page = AuthPage(browser)   # нажимаем на кнопку "Зарегистрироваться"
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)
    page.enter_firstname(valid_firstname)   # вводим валидное имя
    browser.implicitly_wait(5)

    page.enter_lastname(valid_lastname)   # вводим валидную фамилию
    browser.implicitly_wait(5)

    page.enter_email(valid_email)   # вводим валидный адрес электронной почты
    browser.implicitly_wait(3)

    page.enter_password(valid_password)   # вводим валидный пароль
    browser.implicitly_wait(3)

    page.enter_pass_conf(random_password)   # вводим невалидное подтверждение пароля
    browser.implicitly_wait(3)

    page.btn_click()   # нажимаем на кнопку "Зарегистрироваться"
    error_mess = browser.find_element(*AuthLocators.AUTH_MESSAGE_ERROR)
    time.sleep(5)

    assert error_mess.text == "Пароли не совпадают"
    print(f"RTC-037"
          f"\nНегативный сценарий регистрации в личном кабинете РосТелеКом: "
          f"значения в полях ввода 'Пароль' и 'Подтверждение пароля' не совпадают")
    print('Сообщение об ошибке: "Пароли не совпадают"')
