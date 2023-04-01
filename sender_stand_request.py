import configuration
import data
import requests


def post_create_order(body):  # запрос на создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


def get_kit_id_from_create_order_response(res): # получение kit_id после создания заказа
    return res.json()["track"]
