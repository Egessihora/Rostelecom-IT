import json
import requests


class RandomEmail:
    """Класс создаёт временный адрес электронной почты на сайте https://www.1secmail.com
    для дальнейшего проведения автотестов интерфейса личного кабинета РосТелеКом"""
    def __init__(self):
        self.base_url = 'https://www.1secmail.com/api/v1/'

    def get_api_email(self) -> json:
        """ Получаем случайный адрес электронной почты"""
        action = {'action': 'genRandomMailbox', 'count': 1}
        res = requests.get(self.base_url, params=action)
        status_email = res.status_code
        try:
            result_email = res.json()
        except json.decoder.JSONDecodeError:
            result_email = res.text
        return result_email, status_email

    def get_id_letter(self, login: str, domain: str) -> json:
        """ Проверяем mailbox, получаем mail_id"""
        action = {'action': 'getMessages', 'login': login, 'domain': domain}
        res = requests.get(self.base_url, params=action)
        status_id = res.status_code
        try:
            result_id = res.json()
        except json.decoder.JSONDecodeError:
            result_id = res.text
        return result_id, status_id

    def get_reg_code(self, login: str, domain: str, ids: str) -> json:
        """ Получаем письмо с кодом регистрации от Ростелекома (id=ids) """
        action = {'action': 'readMessage', 'login': login, 'domain': domain, 'id': ids}
        res = requests.get(self.base_url, params=action)
        status_code = res.status_code
        result_code = ''
        try:
            result_code = res.json()
        except json.decoder.JSONDecodeError:
            result_code = res.text
        return result_code, status_code
