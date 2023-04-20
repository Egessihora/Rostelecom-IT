import pytest
from selenium import webdriver


# Инициализация браузера и его закрытие по окончанию тестов
@pytest.fixture()
def browser():
    print("\nstart browser for test")
    driver = webdriver.Chrome()  # инициализируем браузер
    yield driver
    print("\nquit browser")
    driver.quit()  # закрываем браузер
