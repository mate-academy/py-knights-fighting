from random import randint


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.base_power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight.get("armour", [])
        self.protection = sum(
            armour_piece["protection"] for armour_piece in self.armour
        )
        self.weapon = knight.get("weapon", {"power": 0})
        self.potion = knight.get("potion")
        self.power = self.base_power + self.weapon["power"]

        self.special_abilities = knight.get("special_abilities", [])

        if self.potion:
            self.apply_potion_effect()

    def apply_potion_effect(self) -> None:
        for effect, value in self.potion.get("effect", {}).items():
            setattr(self, effect, getattr(self, effect, 0) + value)

    def attempt_resurrection(self) -> bool:
        for ability in self.special_abilities:
            if (
                    ability["name"] == "Divine Resurrection"
                    and ability["amount"] > 0
            ):
                roll = randint(1, 100)
                if roll > 95:  # 5% chance
                    self.hp += 50
                    ability["amount"] -= 1
                    print(f"{self.name} has been resurrected!")
                    return True
        return False
