class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_URL = '/api/v1/courier'
    LOGIN_COURIER_URL = '/api/v1/courier/login'
    CREATE_ORDER_URL = '/api/v1/orders'
    GET_LIST_ORDERS_URL = '/api/v1/orders'
    CANCEL_ORDER_URL = '/api/v1/orders/cancel?track='
    DELETE_COURIER_URL = '/api/v1/courier/' # :id - Номер курьера, хранится в поле id таблицы Couriers
