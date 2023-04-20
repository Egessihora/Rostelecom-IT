import os
import time

from pages.Base_APP import BasePage
from pages.settings import base_url
from pages.locators import *


class AuthPage(BasePage):
    """Класс реализует методы для работы с web-элементами на странице авторизации"""
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv(base_url) or 'https://b2c.passport.rt.ru'
        driver.get(url)
        self.tab_email = driver.find_element(*AuthLocators.AUTH_TAB_EMAIL)
        self.tab_phone = driver.find_element(*AuthLocators.AUTH_TAB_PHONE)
        self.tab_login = driver.find_element(*AuthLocators.AUTH_TAB_LOGIN)
        self.tab_ls = driver.find_element(*AuthLocators.AUTH_TAB_LS)
        self.username = driver.find_element(*AuthLocators.AUTH_FIELD_USERNAME)
        self.password = driver.find_element(*AuthLocators.AUTH_FIELD_PASS)
        self.forgot_password = driver.find_element(*AuthLocators.AUTH_BUTTON_FORGOT_PASSWORD)
        self.btn = driver.find_element(*AuthLocators.AUTH_BUTTON_ENTER)
        self.reg_in = driver.find_element(*AuthLocators.AUTH_REG_IN)
        self.auth_by_vk = driver.find_element(*AuthLocators.AUTH_BY_VK)
        self.auth_by_odnoklassniky = driver.find_element(*AuthLocators.AUTH_BY_OK)
        self.auth_by_mail = driver.find_element(*AuthLocators.AUTH_BY_MAIL)
        self.auth_by_google = driver.find_element(*AuthLocators.AUTH_BY_GOOGLE)
        self.auth_by_yandex = driver.find_element(*AuthLocators.AUTH_BY_YANDEX)

    def tab_email(self):
        """Выбирает тип авторизации 'Почта'"""
        self.tab_email()

    def tab_phone(self):
        """Выбирает тип авторизации 'Телефон'"""
        self.tab_phone()

    def tab_login(self):
        """Выбирает тип авторизации 'Логин'"""
        self.tab_login()

    def tab_ls(self):
        """Выбирает тип авторизации 'Лицевой счёт'"""
        self.tab_ls()

    def enter_username(self, value):
        """Вводит адрес электронной почты в поле ввода"""
        self.username.send_keys(value)

    def enter_password(self, value):
        """Вводит пароль в поле ввода"""
        self.password.send_keys(value)

    def forgot_password(self):
        """Нажимает на кнопку 'Забыл пароль'"""
        self.forgot_password()
        time.sleep(10)

    def btn_click_enter(self):
        """Нажимает на кнопку 'Войти'"""
        self.btn.click()
        time.sleep(10)

    def enter_reg_page(self):
        """Нажимает на кнопку 'Зарегистрироваться'"""
        self.reg_in.click()
        time.sleep(10)

    def auth_by_vk(self):
        """Нажимает на иконку авторизации через социальную сеть 'ВКонтакте'"""
        self.auth_by_vk()
        time.sleep(10)

    def auth_by_odnoklassniky(self):
        """Нажимает на иконку авторизации через социальную сеть 'Одноклассники'"""
        self.auth_by_odnoklassniky()
        time.sleep(10)

    def auth_by_mail(self):
        """Нажимает на иконку авторизации через учётную запись в почтовом сервисе mail.ru"""
        self.auth_by_mail()
        time.sleep(10)

    def auth_by_google(self):
        """Нажимает на иконку авторизации через учётную запись в почтовом сервисе google.com"""
        self.auth_by_google()
        time.sleep(10)

    def auth_by_yandex(self):
        """Нажимает на иконку авторизации через учётную запись в почтовом сервисе yandex.ru"""
        self.auth_by_yandex()
        time.sleep(10)


class RegPage(BasePage):
    """Класс реализует методы для работы с web-элементами на странице регистрации"""
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.first_name = driver.find_element(*RegLocators.REG_FIELD_FIRSTNAME)
        self.last_name = driver.find_element(*RegLocators.REG_FIELD_LASTNAME)
        self.email = driver.find_element(*RegLocators.REG_FIELD_EMAIL)
        self.password = driver.find_element(*RegLocators.REG_FIELD_PASS)
        self.pass_conf = driver.find_element(*RegLocators.REG_FIELD_PASS_CONFIRM)
        self.btn = driver.find_element(*RegLocators.REG_BUTTON_SUBMIT)

    def enter_firstname(self, value):
        """Вводит имя в поле ввода"""
        self.first_name.send_keys(value)

    def enter_lastname(self, value):
        """Вводит фамилию в поле ввода"""
        self.last_name.send_keys(value)

    def enter_email(self, value):
        """Вводит адрес электронной почты в поле ввода"""
        self.email.send_keys(value)

    def enter_password(self, value):
        """Вводит пароль в поле ввода"""
        self.password.send_keys(value)

    def enter_pass_conf(self, value):
        """Вводит подтверждение пароля в поле ввода"""
        self.pass_conf.send_keys(value)

    def btn_click(self):
        """Нажимает на кнопку 'Зарегистрироваться'"""
        self.btn.click()


class NewPassPage(BasePage):
    """Класс реализует методы для работы с web-элементами на странице восстановления пароля"""
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'
        driver.get(url)
        self.tab_email = driver.find_element(*NewPassLocators.NEW_PASS_TAB_EMAIL)
        self.tab_phone = driver.find_element(*NewPassLocators.NEW_PASS_TAB_PHONE)
        self.tab_login = driver.find_element(*NewPassLocators.NEW_PASS_TAB_LOGIN)
        self.tab_ls = driver.find_element(*NewPassLocators.NEW_PASS_TAB_LS)
        self.username = driver.find_element(*NewPassLocators.NEW_PASS_FIELD_USERNAME)
        self.btn_continue = driver.find_element(*NewPassLocators.NEW_PASS_BUTTON_CONTINUE)
        self.btn_reload = driver.find_element(*NewPassLocators.NEW_PASS_RELOAD_CAPTCHA)
        self.come_back = driver.find_element(*NewPassLocators.NEW_PASS_BUTTON_BACK)

    def tab_email(self):
        """Выбирает тип восстановления пароля 'Почта'"""
        self.tab_email()

    def tab_phone(self):
        """Выбирает тип восстановления пароля 'Телефон'"""
        self.tab_phone()

    def tab_login(self):
        """Выбирает тип восстановления пароля 'Логин'"""
        self.tab_login()

    def tab_ls(self):
        """Выбирает тип восстановления пароля 'Лицевой счёт'"""
        self.tab_ls()

    def enter_username(self, value):
        """Вводит адрес электронной почты в поле ввода"""
        self.username.send_keys(value)

    def btn_continue(self):
        """Нажимает на кнопку 'Продолжить'"""
        self.btn_continue()

    def btn_reload(self):
        """Нажимает на кнопку обновления изображения символов"""
        self.btn_reload()

    def btn_come_back(self):
        """Нажимает на кнопку 'Вернуться назад'"""
        self.come_back.click()
