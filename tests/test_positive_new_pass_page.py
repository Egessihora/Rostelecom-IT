from pages.RandomEmail_APP import RandomEmail
from pages.RosTeleCom_APP import *
from pages.settings import *
from pages.locators import *
import time
import pytest


# RTC-021
@pytest.mark.reg
@pytest.mark.positive
def test_new_pass_page_open(browser):
    page = AuthPage(browser)
    page.forgot_password.click()
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_page.png")
    print(f"RTC-021 \nПроверка перехода на страницу восстановления пароля в личном кабинете РосТелеКом")
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/reset-credentials"


# RTC-023
@pytest.mark.auth
@pytest.mark.positive
def test_new_pass_tab_email(browser):
    page = NewPassPage(browser)
    page.tab_email.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/New_password/tab_email_click.png")
    print(f"RTC-023 \nПроверка кликабельности таба 'Почта'")
    assert page.tab_email.text == "Почта"


# RTC-024
@pytest.mark.auth
@pytest.mark.positive
def test_new_pass_tab_phone(browser):
    page = NewPassPage(browser)
    page.tab_phone.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/New_password/tab_phone_click.png")
    print(f"RTC-024 \nПроверка кликабельности таба 'Телефон'")
    assert page.tab_phone.text == "Телефон"


# RTC-025
@pytest.mark.auth
@pytest.mark.positive
def test_new_pass_tab_login(browser):
    page = NewPassPage(browser)
    page.tab_login.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/New_password/tab_login_click.png")
    print(f"RTC-025 \nПроверка кликабельности таба 'Логин'")
    assert page.tab_login.text == "Логин"


# RTC-026
@pytest.mark.auth
@pytest.mark.positive
def test_new_pass_tab_ls(browser):
    page = NewPassPage(browser)
    page.tab_ls.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/New_password/tab_ls_click.png")
    print(f"RTC-026 \nПроверка кликабельности таба 'Лицевой счёт'")
    assert page.tab_ls.text == "Лицевой счёт"


# RTC-027
def test_reload_captcha(browser):
    page = NewPassPage(browser)
    browser.implicitly_wait(10)
    page.driver.save_screenshot(r"../tests/screenshots/New_password/first_captcha.png")
    first_captcha = browser.find_element(*NewPassLocators.NEW_PASS_IMAGE_CAPTCHA)
    page.btn_reload.click()
    time.sleep(5)
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_captcha.png")
    new_captcha = browser.find_element(*NewPassLocators.NEW_PASS_IMAGE_CAPTCHA)
    print(f"RTC-027 \nПроверка обновления каптчи на странице восстановления РосТелеКом")

    assert new_captcha != first_captcha


# RTC-028
def test_come_back(browser):
    page = NewPassPage(browser)
    page.btn_come_back()
    print(f"RTC-028 \nПроверка кликабельности кнопки 'Вернуться назад'"
          f"на странице восстановления пароля РосТелеКом")
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/authenticate"


# RTC-029 Восстановление пароля по адресу эл.почты
# Количество итераций в сутки для восстановления пароля ограничено!!!
# В начале теста в поле "Символы" требуется одноразовый ручной ввод CAPTCHA!!!
@pytest.mark.newpass
@pytest.mark.positive
def test_new_pass_by_email(browser):
    # Разделяем email на имя и домен для использования в последующих запросах:
    sign_at = valid_email.find("@")
    mail_name = valid_email[0:sign_at]
    mail_domain = valid_email[sign_at + 1:len(valid_email)]

    page = NewPassPage(browser)
    page.enter_username(valid_email)
    time.sleep(50)  # время на ручной!! ввод символов с картинки
    page.btn_continue.click()

    # Ожидаем поступление письма с кодом восстановления на указанный адрес электронной почты:
    time.sleep(30)

    # Проверяем почтовый ящик на наличие писем и находим ID последнего письма:
    result_id, status_id = RandomEmail().get_id_letter(mail_name, mail_domain)
    id_letter = result_id[0].get("id")
    # Сверяем полученные данные с нашими ожиданиями
    assert status_id == 200, "status_id error"
    assert id_letter > 0, "id_letter > 0 error"

    # Получаем код восстановления из письма от РосТелеКом:
    result_code, status_code = RandomEmail().get_reg_code(mail_name, mail_domain, str(id_letter))

    text_body = result_code.get("body")
    # Извлекаем код из текста методом find:
    reg_code = text_body[text_body.find("Ваш код: ") + len("Ваш код: "):
                         text_body.find("Ваш код: ") + len("Ваш код: ") + 6]
    # Сверяем полученные данные с нашими ожиданиями
    assert status_code == 200, "status_code error"
    assert reg_code != '', "reg_code != [] error"

    reg_digit = [int(char) for char in reg_code]

    browser.implicitly_wait(50)
    for i in range(0, 6):
        browser.find_elements(*NewPassLocators.NEW_PASS_ONETIME_CODE)[i].send_keys(reg_code[i])
        browser.implicitly_wait(5)
    # browser.implicitly_wait(30)
    time.sleep(10)
    new_pass = random_password
    browser.find_element(*NewPassLocators.NEW_PASS_NEW_PASS).send_keys(new_pass)
    time.sleep(3)
    browser.find_element(*NewPassLocators.NEW_PASS_NEW_PASS_CONFIRM).send_keys(new_pass)
    browser.find_element(*NewPassLocators.NEW_PASS_BTN_SAVE).click()
    time.sleep(30)
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_by_email_success.png")
    print(f"RTC-029 \nПроверка восстановления пароля по эл.почте в личном кабинете РосТелеКом")

    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/authenticate"

    # В случае успешной смены пароля, перезаписываем его в файл settings:
    with open(r"../pages/settings.py", "r", encoding="utf8") as file:
        lines = []
        for line in file.readlines():
            if "valid_password" in line:
                lines.append(f"valid_password = '{random_password}'\n")
            else:
                lines.append(line)
    with open(r"../pages/settings.py", "w", encoding="utf8") as file:
        file.writelines(lines)
