from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.person.knight import Knight


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def apply(self, knight: "Knight") -> None:

        if "power" in self.effect:
            knight.power += self.effect["power"]

        if "protection" in self.effect:
            knight.protection += self.effect["protection"]

        if "hp" in self.effect:
            knight.hp += self.effect["hp"]
