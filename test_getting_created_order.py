from data import order_body
from sender_stand_request import create_order_and_get_id, get_order


def test_order_information():
    track_id = create_order_and_get_id(order_body)
    res = get_order(track_id)
    assert 200 == res.status_code
