from src.JSONAdvert import JSONAdvert


def test_empty_json():
    obj = JSONAdvert({})
    dict_obj = obj.__dict__
    assert dict_obj == {}


def test_lesson():
    obj = JSONAdvert({
        'title': 'python', 'price': 0,
        'location': {
            'address': 'город Москва, Лесная, 7',
            'metro_stations': ['Белорусская']
        }
    })
    dict_obj = obj.__dict__
    assert len(dict_obj.keys()) == 3
    assert len(dict_obj['location'].__dict__.keys()) == 2
    assert dict_obj['title'] == 'python'
    assert dict_obj['price'] == 0
    lesson_address = dict_obj['location'].__dict__['address']
    lesson_metro_stations = dict_obj['location'].__dict__['metro_stations']
    assert lesson_address == 'город Москва, Лесная, 7'
    assert lesson_metro_stations == ['Белорусская']
