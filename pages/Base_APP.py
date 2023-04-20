from pages.settings import base_url
from pages.locators import MainPageLocators
from urllib.parse import urlparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Класс реализует в себе необходимые методы для работы с webdriver. Принимает driver — экземпляр webdriver."""
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.base_url = base_url
        self.driver.implicitly_wait(timeout)   # неявное ожидание, по умолчанию на 10 сек.

    def go_to_site(self):
        """Открывает нужную страницу в браузере"""
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        """Находит один элемент и возвращает его"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not find {locator}')

    def find_many_elements(self, locator, time=10):
        """Находит множество элементов и возвращает их список"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Not find {locator}')

    def should_be_menu_autorization(self):
        menu_autorization = self.find_element(*MainPageLocators.PAGE_AUTH)
        result = menu_autorization.text
        assert result == "Авторизация"

    def get_relative_link(self):
        """Получает адрес текущей страницы"""
        url = urlparse(self.driver.current_url)
        return url.path

    def find_element_until_to_be_clickable(self, locator, time=10):
        """Ищет элемент в течение 10сек. до тех пока он не станет кликабельным"""
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Element not clickable!')
