import sender_stand_request

# тест на создание заказа и получение по номеру
def test_create_order():
    order_response = sender_stand_request.post_new_order()
    track = order_response.json()['track']
    order_by_track_response = sender_stand_request.get_order_by_track(track)

    assert order_by_track_response.status_code == 200

