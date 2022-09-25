class ColorizeMixin:
    repr_color_code = 32  # green

    def __str__(self):
        temp = self.__repr__()
        return f'\033[{self.repr_color_code}m{temp}\033[0;0m'
