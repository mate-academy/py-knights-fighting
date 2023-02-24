from typing import Union


class Knight:
    def __init__(self, info: dict) -> None:
        self.name = info["name"]
        self.power = info["power"]
        self.hp = info["hp"]
        self.protection = 0
        self.preparing(info)

    def __setitem__(self, key: str, value: Union[int, str]) -> None:
        self.__dict__[key] = value

    def __getitem__(self, key: str) -> Union[int, str]:
        return self.__dict__[key]

    def preparing(self, info: dict) -> None:
        self.power += info["weapon"]["power"]

        if info["armour"]:
            for part in info["armour"]:
                self.protection += part["protection"]

        if info["potion"] is not None:
            for effect in info["potion"]["effect"]:
                self[effect] += info["potion"]["effect"].get(effect, 0)
