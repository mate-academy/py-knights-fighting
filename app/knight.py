class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0
        Knight.ready_to_fight(self)

    def add_weapon(self) -> None:
        self.power += self.weapon["power"]

    def add_protection(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]

    def add_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            Knight.check_hp(self)

    def ready_to_fight(self) -> None:
        Knight.add_protection(self)
        Knight.add_weapon(self)
        Knight.add_potion(self)

    def check_hp(self) -> None:
        if self.hp < 0:
            self.hp = 0
