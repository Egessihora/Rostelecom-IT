import pytest
from pages.RandomEmail_APP import RandomEmail
from pages.RosTeleCom_APP import *
from selenium.webdriver.common.by import By
from pages.settings import *


# RTC-016
@pytest.mark.reg
@pytest.mark.positive
def test_reg_page_open(browser):
    page = AuthPage(browser)
    page.enter_reg_page()
    page.driver.save_screenshot(r"../tests/screenshots/Registration/registration_page.png")
    print(f"RTC-016 \nПроверка успешного перехода на страницу регистрации РосТелеКом")
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"


# RTC-020
@pytest.mark.reg
@pytest.mark.positive
class TestRegistration:
    """Класс проверяет успешную регистрацию в личном кабинете РосТелеКом.
    Для регистрации используется временный адрес электронной почты, получаемый в классе RandomEmail
    с помощью сайта https://www.1secmail.com.
    Класс получает код для входа на почтовый ящик и записывает сгенерированный временный электронный адрес
    в файл settings.py.
    В теле класса определяем данные для доступа к их значениям из всех методов классса."""
    result_email, status_email = RandomEmail().get_api_email()  # запрос на получение временного адреса эл.почты
    valid_email = result_email[0]  # из запроса получаем валидный email

    def test_get_registration_by_email(self, browser):
        # Разделяем email на имя и домен для использования в последующих запросах:
        sign_at = self.valid_email.find('@')
        mail_name = self.valid_email[0:sign_at]
        mail_domain = self.valid_email[sign_at + 1:len(self.valid_email)]
        assert self.status_email == 200, 'status_email error'
        assert len(self.result_email) > 0, 'len(result_email) > 0 -> error'

        # Активируем окно регистрации, нажимаем на кнопку "Зарегистрироваться":
        page = AuthPage(browser)
        page.enter_reg_page()
        browser.implicitly_wait(2)
        assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

        page = RegPage(browser)

        browser.implicitly_wait(5)
        page.enter_firstname(valid_firstname)  # вводим имя
        browser.implicitly_wait(5)

        page.enter_lastname(valid_lastname)  # вводим фамилию
        browser.implicitly_wait(5)

        enter_region = browser.find_elements(By.CSS_SELECTOR, "input.rt-input__input")
        enter_region[2].send_keys(valid_region)   # вводим регион

        page.enter_email(self.valid_email)  # вводим адрес электронной почты
        browser.implicitly_wait(3)

        page.enter_password(valid_password)  # вводим пароль
        browser.implicitly_wait(3)

        page.enter_pass_conf(valid_password)  # вводим подтверждение пароля
        browser.implicitly_wait(3)

        page.btn_click()  # нажимаем на кнопку "Зарегистрироваться"
        # Ожидаем поступление письма с кодом подтверждения на указанный адрес электронной почты:
        time.sleep(30)

        # Проверяем почтовый ящик на наличие писем и находим ID последнего письма:
        result_id, status_id = RandomEmail().get_id_letter(mail_name, mail_domain)
        id_letter = result_id[0].get('id')
        # Сверяем полученные данные с нашими ожиданиями:
        assert status_id == 200, "status_id error"
        assert id_letter > 0, "id_letter > 0 error"

        # Получаем код регистрации из письма от РосТелеКом:
        result_code, status_code = RandomEmail().get_reg_code(mail_name, mail_domain, str(id_letter))

        text_body = result_code.get("body")
        # Извлекаем код из текста методом find:
        reg_code = text_body[text_body.find("Ваш код : ") + len("Ваш код : "):
                             text_body.find("Ваш код : ") + len("Ваш код : ") + 6]
        # Сверяем полученные данные с нашими ожиданиями:
        assert status_code == 200, "status_code error"
        assert reg_code != '', "reg_code != [] error"

        # Вводим полученный код в соответствующее поле ввода:
        [int(char) for char in reg_code]
        browser.implicitly_wait(30)
        for i in range(0, 6):
            browser.find_elements(By.CSS_SELECTOR, "input[inputmode='numeric']")[i].send_keys(reg_code[i])
            browser.implicitly_wait(5)
        browser.implicitly_wait(30)

        # Проверяем, что регистрация успешно пройдена и пользователь перенаправлен
        # в свой личный кабинет на сайте РосТелеКом:
        assert page.get_relative_link() == "/account_b2c/page"
        time.sleep(10)

        # При успешной регистрации, перезаписываем временный email в файл settings.py:
        page.driver.save_screenshot(r"../tests/screenshots/Registration/registration_sucсess.png")
        print(f"RTC-020 \nПроверка успешной регистрации в личном кабинете РосТелеКом")
        with open(r"../pages/Settings.py", "r", encoding="utf8") as file:
            lines = []
            for line in file.readlines():
                if "valid_email" in line:
                    lines.append(f'valid_email = "{str(self.valid_email)}"\n')
                else:
                    lines.append(line)
        with open(r"../pages/Settings.py", "w", encoding="utf8") as file:
            file.writelines(lines)
