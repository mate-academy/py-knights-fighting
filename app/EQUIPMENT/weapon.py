from typing import Union


class Weapon:
    def __init__(self, data: dict[str, Union[str, int]]) -> None:
        self.name = data["name"]
        self.power = data["power"]
