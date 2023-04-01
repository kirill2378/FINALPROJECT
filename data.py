headers = {
    "Content-Type": "application/json"
}

order_body = {
    "firstName": "Иван",
    "lastName": "Петров",
    "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
    "metroStation": 204,
    "phone": "+9998887766",
    "rentTime": 5,
    "deliveryDate": "2023-03-29",
    "comment": "",
    "color": [
        "BLACK"
    ]
}

response_body_order = {
    "track": 124124
}

number_body = {
         "order": {
             "id": 2,
             "firstName": "Naruto",
             "lastName": "Uzumaki",
             "address": "Kanoha, 142 apt.",
             "metroStation": "1",
             "phone": "+7 800 355 35 35",
             "rentTime": 5,
             "deliveryDate": "2020-06-06T00:00:00.000Z",
             "track": 521394,
             "status": 1,
             "color": [
                 "BLACK"
             ],
             "comment": "Saske, come back to Kanoha",
             "cancelled": "false",
             "finished": "false",
             "inDelivery": "false",
             "courierFirstName": "Kaneki",
             "createdAt": "2020-06-08T14:40:28.219Z",
             "updatedAt": "2020-06-08T14:40:28.219Z"
  }
}
