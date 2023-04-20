from selenium.webdriver.common.by import By


class AuthLocators:
    """Локаторы страницы авторизации"""
    AUTH_TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    AUTH_FIELD_USERNAME = (By.ID, "username")
    AUTH_FIELD_PASS = (By.ID, "password")
    AUTH_BUTTON_ENTER = (By.ID, "kc-login")
    AUTH_REG_IN = (By.ID, "kc-register")
    AUTH_BUTTON_FORGOT_PASSWORD = (By.ID, "forgot_password")
    AUTH_MESSAGE_ERROR = (By.CLASS_NAME, "rt-input-container__meta--error")
    AUTH_FORM_ERROR = (By.ID, "form-error-message")
    AUTH_TAB_PHONE = (By.ID, "t-btn-tab-phone")
    AUTH_TAB_LS = (By.ID, "t-btn-tab-ls")
    AUTH_TAB_LOGIN = (By.ID, "t-btn-tab-login")
    AUTH_BY_VK = (By.ID, "oidc_vk")
    AUTH_BY_OK = (By.ID, "oidc_ok")
    AUTH_BY_MAIL = (By.ID, "oidc_mail")
    AUTH_BY_GOOGLE = (By.ID, "oidc_google")
    AUTH_BY_YANDEX = (By.ID, "oidc_ya")
    AUTH_TAB = (By.CSS_SELECTOR, ".rt-tab.rt-tab--small.rt-tab--active")


class RegLocators:
    """Локаторы страницы регистрации"""
    REG_FIELD_FIRSTNAME = (By.CSS_SELECTOR, "input[name='firstName']")
    REG_FIELD_LASTNAME = (By.CSS_SELECTOR, "input[name='lastName']")
    REG_FIELD_EMAIL = (By.ID, "address")
    REG_FIELD_PASS = (By.ID, "password")
    REG_FIELD_PASS_CONFIRM = (By.CSS_SELECTOR, "input[id='password-confirm']")
    REG_BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type='submit'")
    REG_CARD_MODAL = (By.CLASS_NAME, "card-modal__title")


class NewPassLocators:
    """Локаторы страницы восстановления пароля"""
    NEW_PASS_TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    NEW_PASS_TAB_PHONE = (By.ID, "t-btn-tab-phone")
    NEW_PASS_TAB_LOGIN = (By.ID, "t-btn-tab-login")
    NEW_PASS_TAB_LS = (By.ID, "t-btn-tab-ls")
    NEW_PASS_FIELD_USERNAME = (By.ID, "username")
    NEW_PASS_BUTTON_CONTINUE = (By.ID, "reset")
    NEW_PASS_ONETIME_CODE = (By.CSS_SELECTOR, "input[inputmode='numeric']")
    NEW_PASS_NEW_PASS = (By.ID, "password-new")
    NEW_PASS_NEW_PASS_CONFIRM = (By.ID, "password-confirm")
    NEW_PASS_BTN_SAVE = (By.CSS_SELECTOR, "button[id='t-btn-reset-pass']")
    NEW_PASS_MESSAGE_ERROR = (By.ID, "form-error-message")
    NEW_PASS_MESSAGE_ERROR_EMAIL = (By.CLASS_NAME, "rt_input-container__meta--error")
    NEW_PASS_IMAGE_CAPTCHA = (By.CLASS_NAME, "rt-captcha__image")
    NEW_PASS_RELOAD_CAPTCHA = (By.CLASS_NAME, "rt-captcha__reload")
    NEW_PASS_BUTTON_BACK = (By.ID, "reset-back")


class MainPageLocators:
    """Локатор страницы авторизации РосТелеКом"""
    PAGE_AUTH = (By.ID, "page-right")
