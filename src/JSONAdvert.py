from keyword import iskeyword
from typing import Mapping


class JSONAdvert:
    def __set_attr(self, mapping: Mapping):
        """Динамически инициализирует атрибуты из словаря mapping
        Если под каким-то ключем скрывается новый словарь, то """
        for key, value in mapping.items():
            attr_key = key + '_' if iskeyword(key) else key
            if isinstance(mapping[key], Mapping):
                attr_obj = JSONAdvert(mapping[key])
            else:
                attr_obj = mapping[key]
            self.__setattr__(attr_key, attr_obj)

    def __init__(self, json_obj):
        self.__set_attr(json_obj)
