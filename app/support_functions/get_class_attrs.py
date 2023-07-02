from inspect import signature as sgt
from typing import Type


class TestClass:
    def __init__(self, value: int) -> None:
        self.value = value


def get_class_attribute(cls: Type) -> dict:
    """This function gets class attrs name, for using they
    for create class object with other same dict parameters keys."""
    class_init_sign = sgt(cls.__init__).parameters
    return {
        attr_name: None
        for attr_name in class_init_sign
        if attr_name != "self"
    }


if __name__ == '__main__':
    print(get_class_attribute(TestClass))
