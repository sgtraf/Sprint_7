class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_URL = '/api/v1/courier'
    LOGIN_COURIER_URL = '/api/v1/courier/login'
    CREATE_ORDER_URL = '/api/v1/orders'
    GET_LIST_ORDERS_URL = '/api/v1/orders'
    CANCEL_ORDER_URL = '/api/v1/orders/cancel?track='
    DELETE_COURIER_URL = '/api/v1/courier/' # :id - Номер курьера, хранится в поле id таблицы Couriers
    TAKE_ORDER_URL = '/api/v1/orders/accept/:id' # :id - Номер заказа, хранится в поле id таблицы Orders
    GET_ORDER_BY_NUMBER = '/api/v1/orders/track' # track - Трекинговый номер заказа

class OrderData:
    Order1 = {
         "firstName": "Naruto",
         "lastName": "Uchiha",
         "address": "Konoha, 142 apt.",
         "metroStation": 4,
         "phone": "+7 800 355 35 35",
         "rentTime": 5,
         "deliveryDate": "2025-06-06",
         "color": ['BLACK', ''],
         "comment": "Saske, come back to Konoha"

    }

    Order2 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-06-08",
        "comment": "Saske, come back to Konoha",
        "color": [
            "GREY", ''
        ]
    }

    Order3 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-06-08",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK", "GREY"
        ]
    }

    Order4 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-06-09",
        "comment": "Saske, come back to Konoha",
        "color": [
        ]
    }

    ORDERS = [Order1, Order2, Order3, Order4]
