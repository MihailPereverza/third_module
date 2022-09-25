from src.JSONAdvert import JSONAdvert
from src.advert import Advert


def test_min_json():
    advert = Advert({'title': 'Python'})
    advert_str = advert.__repr__()
    assert advert_str == 'Python | 0 ₽'
    assert len(advert.__dict__.keys()) == 2
    assert advert.price == 0


def test_negative_price():
    advert = Advert({'title': 'Python', 'price': -100500})
    advert_str = advert.__repr__()
    assert advert_str == 'Python | 0 ₽'
    assert len(advert.__dict__.keys()) == 2
    assert advert.price == 0


def correct_inheritance_json_advert():
    lesson = JSONAdvert({
        'title': 'python', 'price': 0,
        'location': {
            'address': 'город Москва, Лесная, 7',
            'metro_stations': ['Белорусская']
        }
    })
    lesson_dict = lesson.__dict__
    assert len(lesson_dict.keys()) == 3
    assert len(lesson_dict['location'].__dict__.keys()) == 2
    assert lesson_dict['title'] == 'python'
    assert lesson_dict['price'] == 0
    lesson_address = lesson_dict['location'].__dict__['address']
    lesson_metro_stations = lesson_dict['location'].__dict__['metro_stations']
    assert lesson_address == 'город Москва, Лесная, 7'
    assert lesson_metro_stations == ['Белорусская']
