from dataclasses import dataclass


@dataclass
class Weapon:
    name: str
    power: int

    @classmethod
    def create(cls, knight: dict) -> "Weapon":
        return cls(knight["weapon"]["name"],
                   knight["weapon"]["power"])
