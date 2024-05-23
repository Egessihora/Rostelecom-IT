## Итоговый проект по автоматизации тестирования
### Объект тестирования: [Ростелеком Информационные Технологии](https://b2c.passport.rt.ru)
___
В рамках проекта произведено ручное и автоматизированное тестирование нового интерфейса авторизации в личном кабинете с применением PyTest и Selenium Webdriver

Тесты проверяют:
* Авторизацию в личном кабинете
* Регистрацию в личном кабинете
* Восстановление пароля в личном кабинете
___
Сформированы тест-кейсы и отчёты о дефектах: [смотреть здесь](https://docs.google.com/spreadsheets/d/1aZWL0gVnk_XShbtlnsnQKIZt6Dn730fDVJlYXYJ-h-U/edit?usp=sharing)
___
Для тестирования интерфейса были использованы:

✅разбиение на классы эквивалентности

✅анализ граничных значений

✅тестирование состояний и переходов

___
**В корневой директории расположены:**
* файл conftest.py - содержит фикстуру для инициализации браузера и закрытия сессии после завершения теста
* файл requirements.txt - список внешних зависимостей
* pytest.ini - регистрация маркеров

**В директории /pages расположены:**
* Base_APP.py - необходимые методы для работы с webdriver
* locators.py - локаторы web-элементов
* RandomEmail_APP.py - GET-запросы к временному почтовому ящику на сайте [1secmail.com](https://www.1secmail.com/) для получения валидного E-mail и кода для регистрации на странице/восстановления пароля
* RosTeleCom_APP.py - необходимые методы для работы с web-элементами на страницах авторизации, регистрации и восстановления пароля
* settings.py - исходные статические данные и учётные данные, используемые в проведении тестирования

**В директории /tests расположены:**
* test_positive_reg_page.py - автоматизированные тесты с позитивными сценариями страницы регистрации
* test_positive_auth_page.py - автоматизированные тесты с позитивными сценариями страницы авторизации
* test_positive_new_pass_page.py - автоматизированные тесты с позитивными сценариями страницы восстановления пароля
* test_negative_reg_page.py - автоматизированные тесты с негативными сценариями страницы регистрации
* test_negative_auth_page.py - автоматизированные тесты с негативными сценариями страницы авторизации
* test_negative_new_pass_page.py - автоматизированные тесты с негативными сценариями страницы восстановления пароля

**В директории /tests/screenshots** расположены графические файлы с фиксацией результата тестирования
___

#### Тесты настроены на запуск через Run!

Окружение: Windows 11 Домашняя версия 21H2

Браузер: Google Chrome 112.0.5615.138 (64-bit)
