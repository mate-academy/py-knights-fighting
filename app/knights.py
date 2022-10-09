from app.equipment import Armor, Weapon, Potion


class Knights:
    def __init__(self, knights: dict) -> None:
        self.knights = knights
        self.name = knights["name"]
        self.power = knights["power"]
        self.hp = knights["hp"]
        self.protection = 0

    def battle_preparation(self) -> None:
        armor = Armor(self.knights["armour"]).apply_armor()
        weapon = Weapon(self.knights["weapon"]).get_weapon()
        potion = Potion(self.knights["potion"]).drink_potion()

        self.power += weapon + potion[0]
        self.hp += potion[1]
        self.protection += armor + potion[2]
