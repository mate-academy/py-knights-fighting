class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def apply_armour(self) -> None:
        if self.armour:
            for item in self.armour:
                self.protection += item["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if self.potion["effect"].get("power"):
                self.power += self.potion["effect"]["power"]
            if self.potion["effect"].get("hp"):
                self.hp += self.potion["effect"]["hp"]
            if self.potion["effect"].get("protection"):
                self.protection += self.potion["effect"]["protection"]

    def battle_preparation(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def fell_in_battle(self) -> None:
        if self.hp <= 0:
            self.hp = 0
