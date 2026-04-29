class Weapon:
    def __init__(self, weapon_dict: dict) -> None:
        self._name = weapon_dict["name"]
        self._power = weapon_dict["power"]

    @property
    def power(self) -> int:
        return self._power

    @property
    def name(self) -> str:
        return self._name
