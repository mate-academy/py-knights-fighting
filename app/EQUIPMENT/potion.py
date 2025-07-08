from typing import Union


class Potion:
    def __init__(self, data: dict[str, Union[str, dict[str, int]]]) -> None:
        self.name = data["name"]
        self.effect = data["effect"]
