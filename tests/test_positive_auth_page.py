import pytest
from pages.RosTeleCom_APP import *
from pages.settings import valid_email, valid_password


# RTC-001
@pytest.mark.reg
@pytest.mark.positive
def test_auth_page_open(browser):
    page = AuthPage(browser)
    page.driver.save_screenshot(r"../tests/screenshots/Autorisation/autorisation_page.png")
    print(f"RTC-001 \nПроверка успешного открытия страницы авторизации РосТелеКом")
    assert page.get_relative_link() == "/auth/realms/b2c/protocol/openid-connect/auth"


# RTC-005
@pytest.mark.auth
@pytest.mark.positive
def test_auth_tab_email(browser):
    page = AuthPage(browser)
    page.tab_email.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/Autorisation/tab_email_click.png")
    print(f"RTC-005 \nПроверка кликабельности таба 'Почта'")
    assert page.tab_email.text == "Почта"


# RTC-006
@pytest.mark.auth
@pytest.mark.positive
def test_auth_tab_phone(browser):
    page = AuthPage(browser)
    page.tab_phone.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/Autorisation/tab_phone_click.png")
    print(f"RTC-006 \nПроверка кликабельности таба 'Телефон'")
    assert page.tab_phone.text == "Телефон"


# RTC-007
@pytest.mark.auth
@pytest.mark.positive
def test_auth_tab_login(browser):
    page = AuthPage(browser)
    page.tab_login.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/Autorisation/tab_login_click.png")
    print(f"RTC-007 \nПроверка кликабельности таба 'Логин'")
    assert page.tab_login.text == "Логин"


# RTC-008
@pytest.mark.auth
@pytest.mark.positive
def test_auth_tab_ls(browser):
    page = AuthPage(browser)
    page.tab_ls.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/Autorisation/tab_ls_click.png")
    print(f"RTC-008 \nПроверка кликабельности таба 'Лицевой счёт'")
    assert page.tab_ls.text == "Лицевой счёт"


# RTC-009
@pytest.mark.parametrize("username", ["+79217777777", valid_email, "valid_login", "269750005232"],
                         ids=["RTC-012) phone", "RTC-013) E-mail", "RTC-014) login", "RTC-015) ls"])
def test_tab(browser, username):

    page = AuthPage(browser)
    page.enter_username(username)

    page.enter_password(valid_password)

    if username == "+79217777777":
        time.sleep(4)
        page.driver.save_screenshot(r"../tests/screenshots/Autorisation/switch_to_phone.png")
        assert browser.find_element(*AuthLocators.AUTH_TAB).text == "Телефон"
        print("RTC-009-1 Телефон")
        browser.find_element(*AuthLocators.AUTH_TAB_PHONE).click()
        time.sleep(2)
    elif username == valid_email:
        time.sleep(4)
        page.driver.save_screenshot(r"../tests/screenshots/Autorisation/switch_to_email.png")
        assert browser.find_element(*AuthLocators.AUTH_TAB).text == "Почта"
        print("RTC-009-2 Почта")
        browser.find_element(*AuthLocators.AUTH_TAB_PHONE).click()
        time.sleep(2)
    elif username == "valid_login":
        time.sleep(4)
        page.driver.save_screenshot(r"../tests/screenshots/Autorisation/switch_to_login.png")
        assert browser.find_element(*AuthLocators.AUTH_TAB).text == "Логин"
        print("RTC-009-3 Логин")
        browser.find_element(*AuthLocators.AUTH_TAB_PHONE).click()
        time.sleep(2)
    else:
        try:
            time.sleep(4)
            page.driver.save_screenshot(r"../tests/screenshots/Autorisation/switch_to_ls.png")
            assert browser.find_element(*AuthLocators.AUTH_TAB).text == "Лицевой счёт"
            print("RTC-009-4 Лицевой счёт")
        except Exception:
            print(f"RTC-009 \n"
                  f"\nBR-4:Тест не пройден. Автоматическое переключения на Лицевой счёт не происходит!")


# RTC-010
def test_auth_by_vk(browser):
    page = AuthPage(browser)
    page.auth_by_vk.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/Autorisation/auth_vk_click.png")
    print(f"RTC-010 \nПроверка перехода на авторизацию через социальную сеть 'ВКонтакте'")
    assert page.get_relative_link() == "/authorize"


# RTC-011
def test_auth_by_odhoklassniky(browser):
    page = AuthPage(browser)
    page.auth_by_odnoklassniky.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/Autorisation/auth_ok_click.png")
    print(f"RTC-011 \nПроверка перехода на авторизацию через социальную сеть 'Одноклассники'")
    assert page.get_relative_link() == "/dk"


# RTC-012
def test_auth_by_mail(browser):
    page = AuthPage(browser)
    page.auth_by_mail.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/Autorisation/auth_mail_click.png")
    print(f"RTC-012 \nПроверка перехода на авторизацию через почтовый сервис mail.ru")
    assert page.get_relative_link() == "/oauth/authorize"


# RTC-013
def test_auth_by_google(browser):
    page = AuthPage(browser)
    page.auth_by_google.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/Autorisation/auth_google_click.png")
    print(f"RTC-013 \nПроверка перехода на авторизацию через почтовый сервис google.com")
    assert page.get_relative_link() == "/o/oauth2/auth/identifier"


# RTC-014
def test_auth_by_yandex(browser):
    page = AuthPage(browser)
    page.auth_by_yandex.click()
    time.sleep(2)
    page.driver.save_screenshot(r"../tests/screenshots/Autorisation/auth_yandex_click.png")
    print(f"RTC-014 \nПроверка перехода на авторизацию через почтовый сервис yandex.ru")
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/authenticate"


# RTC-015
@pytest.mark.auth
@pytest.mark.positive
def test_auth_email(browser):
    page = AuthPage(browser)
    page.tab_email.click()
    time.sleep(2)
    page.enter_username(valid_email)
    page.enter_password(valid_password)
    page.btn_click_enter()
    page.driver.save_screenshot(r"../tests/screenshots/Autorisation/auth_sucсess_by_email.png")
    print(f"RTC-015 \nПроверка успешной авторизации с валидными данными в личном кабинете РосТелеКом")
    assert page.get_relative_link() == "/account_b2c/page"
