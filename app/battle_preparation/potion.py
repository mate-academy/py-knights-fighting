from app.battle_preparation.knight import Knight


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def drink_potion(cls, potion: dict) -> "Potion":
        if potion:
            return cls(potion["name"], potion["effect"])

    def consider_potion_effect(self, knight: Knight) -> None:
        if "hp" in self.effect:
            knight.hp += self.effect["hp"]
        if "power" in self.effect:
            knight.power += self.effect["power"]
        if "protection" in self.effect:
            knight.protection += self.effect["protection"]
        knight.liquid = self.name
