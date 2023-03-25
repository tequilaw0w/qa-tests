import configuration
import requests
import data

# функция выполняет запрос на создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_PATH,
                         json=data.create_order_data,
                         headers=data.common_headers)

# функция получает заказ по номеру
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH,
                         params={'t': track},
                         json=data.create_order_data,
                         headers=data.common_headers)
