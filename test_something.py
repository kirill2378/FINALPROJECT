from create_kit_name import get_number_order


def test_something():
    res = get_number_order()
    assert 200 == res.status_code
