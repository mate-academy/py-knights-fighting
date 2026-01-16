from app.equipment import Armour, Weapon, Potion


class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"] + knight_data["weapon"]["power"]
        self.hp = knight_data["hp"]
        self.armour = [Armour(armour) for armour in knight_data["armour"]]
        self.weapon = Weapon(knight_data["weapon"])
        self.potion = Potion(knight_data["potion"])
        self.protection = 0

    def prepare_for_battle(self) -> None:
        if self.armour:
            for armour in self.armour:
                self.protection += armour.protection
        if hasattr(self.potion, "effects"):
            if self.potion.effects.get("power"):
                self.power += self.potion.effects.get("power")
            if self.potion.effects.get("hp"):
                self.hp += self.potion.effects.get("hp")
            if self.potion.effects.get("protection"):
                self.protection += self.potion.effects.get("protection")

    def fight(self, rival: "Knight") -> None:
        self.hp -= rival.power - self.protection
        rival.hp -= self.power - rival.protection
        if self.hp <= 0:
            self.hp = 0
        if rival.hp <= 0:
            rival.hp = 0
