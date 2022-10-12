class Armor:
    def __init__(self, armour: list) -> None:
        self.armour = armour

    def apply_armor(self) -> int:
        return sum(part["protection"] for part in self.armour)


class Weapon:
    def __init__(self, weapon: dict) -> None:
        self.weapon = weapon

    def get_weapon(self) -> int:
        return self.weapon["power"]


class Potion:
    def __init__(self, potion: dict) -> None:
        self.potion = potion

    def drink_potion(self) -> list:
        potion_effect = [0, 0, 0]

        if self.potion:
            effect = self.potion["effect"]
        else:
            return potion_effect

        if effect.get("power"):
            potion_effect[0] += effect["power"]
        if effect.get("hp"):
            potion_effect[1] = effect["hp"]
        if effect.get("protection"):
            potion_effect[2] = effect["protection"]

        return potion_effect
