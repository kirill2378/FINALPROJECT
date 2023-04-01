import configuration
import data
import requests
import sender_stand_request


def get_number_order():  # запрос на список заказа по номеру
    res = sender_stand_request.post_create_order(data.order_body)
    kit_id = sender_stand_request.get_kit_id_from_create_order_response(res)

    res = requests.get(configuration.URL_SERVICE + configuration.DATA_ORDER + str(kit_id))

    print(res.json()) # можно убрать вывод в консоль
    print(res.status_code) # можно убрать вывод в консоль
    return res


get_number_order()
