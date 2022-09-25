from src.JSONAdvert import JSONAdvert
from src.mixins.colorize_mixin import ColorizeMixin


class Advert(ColorizeMixin, JSONAdvert):
    def __init__(self, *args):
        self._price = 0

        # инициализация через Mapping или через (title, price)
        if len(args) == 1:
            super().__init__(args[0])
        else:
            self.__construct_by_attr(*args)

        self._price = max(0, self._price)

    def __construct_by_attr(self, title, price):
        self._price = price
        self._title = title

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        self._price = max(value, 0)

    def __repr__(self):
        return f'{self.title} | {self._price} ₽'
