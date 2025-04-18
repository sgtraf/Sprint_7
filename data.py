class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_URL = '/api/v1/courier'
    LOGIN_COURIER_URL = '/api/v1/courier/login'
    CREATE_ORDER_URL = '/api/v1/orders'
    GET_LIST_ORDERS_URL = '/api/v1/orders'
    DELETE_COURIER_URL = '/api/v1/courier/:id' # :id - Номер курьера, хранится в поле id таблицы Couriers
    TAKE_ORDER_URL = '/api/v1/orders/accept/:id' # :id - Номер заказа, хранится в поле id таблицы Orders
    GET_ORDER_BY_NUMBER = '/api/v1/orders/track' # track - Трекинговый номер заказа
