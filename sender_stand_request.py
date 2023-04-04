import configuration
import data
import requests


# Отправляем запрос на создание заказа. Возвращаем из функции номер заказа
def create_order_and_get_id(body):
    res = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                        json=body,
                        headers=data.headers)
    return res.json()['track']


# Отправляем запрос для получения статуса созданного заказа
def get_order(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.DATA_ORDER + '?t=' + str(track_id),
                        headers=data.headers)

