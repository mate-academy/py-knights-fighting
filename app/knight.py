from app.ammunition import Ammunition


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0
        self.ammunition = Ammunition(
            weapon=knight["weapon"],
            armour=knight["armour"],
            potion=knight["potion"]
        )
        self.apply_ammunition_effect()

    def apply_ammunition_effect(self) -> None:
        self.ammunition.ammunition_effect()
        self.power += self.ammunition.effects["power"]
        self.hp += self.ammunition.effects["hp"]
        self.protection += self.ammunition.effects["protection"]

    def __repr__(self) -> str:
        return f"name: {self.name}, " \
               f"power: {self.power}, " \
               f"hp: {self.hp}, " \
               f"protection: {self.protection}"
