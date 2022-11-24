class Ammunition:
    def __init__(self, weapon: dict, armour: list, potion: dict) -> None:
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        self.effects = {
            "power": 0,
            "hp": 0,
            "protection": 0
        }

    def armour_effect(self) -> None:
        if not self.armour:
            return
        protection_effect = sum(
            [part["protection"] for part in self.armour]
        )
        self.effects["protection"] += protection_effect

    def weapon_effect(self) -> None:
        self.effects["power"] += self.weapon["power"]

    def potion_effect(self) -> None:
        if not self.potion:
            return
        for effect_name in self.potion["effect"]:
            self.effects[effect_name] += self.potion["effect"][effect_name]

    def ammunition_effect(self) -> None:
        self.potion_effect()
        self.weapon_effect()
        self.armour_effect()
