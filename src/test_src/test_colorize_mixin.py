from pytest import fixture

from src.mixins.colorize_mixin import ColorizeMixin


@fixture
def test_colorize_class():
    class TestClass(ColorizeMixin):
        def __repr__(self):
            return 'test work colorize mixin'

    return TestClass()


def test_colorize(test_colorize_class):
    test_repr = test_colorize_class.__repr__()
    test_str = test_colorize_class.__str__()
    test_color = test_colorize_class.repr_color_code
    assert f'\033[{test_color}m{test_repr}\033[0;0m' == test_str
