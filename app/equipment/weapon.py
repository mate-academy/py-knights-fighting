from __future__ import annotations


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __repr__(self) -> str:
        return (
            f"Weapon("
            f"name = '{self.name}', "
            f"power = {self.power}"
            f")"
        )

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def create_from_dict(cls, data: dict) -> Weapon | None:
        if not data:
            return None

        name = data.get("name", "")
        power = data.get("power", 0)

        return cls(name, power)
