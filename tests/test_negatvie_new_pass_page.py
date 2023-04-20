import pytest
from pages.RosTeleCom_APP import *
from pages.settings import *
import time


# RTC-038
@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_wrong_captcha(browser):
    page = NewPassPage(browser)
    page.enter_username(valid_email)   # вводим адрес электронной почты
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной!! ввод любых символов отличных от символов с картинки
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_by_wrong_captcha.png")
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"
    print(f"RTC-038"
          f"\nНегативный сценарий восстановления пароля по адресу электронной почты: неверные символы с картинки")
    print('Сообщение об ошибке: "Неверный логин или текст с картинки"')


# RTC-039
@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_wrong_email(browser):
    page = NewPassPage(browser)
    page.enter_username(random_email)   # вводим невалидный адрес электронной почты
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной!! ввод символов с картинки
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_by_wrong_email.png")
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"
    print(f"RTC-039"
          f"\nНегативный сценарий восстановления пароля по адресу электронной почты: "
          f"невалидный адрес электронной почты")
    print('Сообщение об ошибке: "Неверный логин или текст с картинки"')


# RTC-040
@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_wrong_phone(browser):
    page = NewPassPage(browser)
    page.enter_username(invalid_phone)   # вводим невалидный номер мобильного телефона
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной!! ввод символов с картинки
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_by_wrong_phone.png")
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"
    print(f"RTC-040"
          f"\nНегативный сценарий восстановления пароля по номеру телефона: "
          f"невалидный номер мобильного телефона")
    print('Сообщение об ошибке: "Неверный логин или текст с картинки"')


# RTC-041
@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_wrong_login(browser):
    page = NewPassPage(browser)
    page.enter_username(invalid_login)   # вводим невалидный логин
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной!! ввод символов с картинки
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_by_wrong_login.png")
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"
    print(f"RTC-041"
          f"\nНегативный сценарий восстановления пароля по логину: "
          f"невалдиный логин")
    print('Сообщение об ошибке: "Неверный логин или текст с картинки"')


# RTC-042
@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_wrong_ls(browser):
    page = NewPassPage(browser)
    page.tab_ls.click()
    browser.implicitly_wait(2)
    page.enter_username(invalid_ls)   # вводим невалидный номер лицевого счёта
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной!! ввод символов с картинки
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_by_wrong_ls.png")
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"
    print(f"RTC-042"
          f"\nНегативный сценарий восстановления пароля по номеру лицевого счёта: "
          f"невалидный лицевой счёт")
    print('Сообщение об ошибке: "Неверный логин или текст с картинки"')
