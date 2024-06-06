class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.protection = 0
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

    def add_power(self) -> None:
        self.power += self.get_additional_power()

    def add_protection(self) -> None:
        self.protection += self.get_additional_protection()

    def add_hp(self) -> None:
        self.hp += self.get_additional_hp()

    def get_additional_power(self) -> int:
        total_additional_power = 0
        total_additional_power += self.weapon["power"]
        if self.potion:
            total_additional_power += self.potion["effect"].get("power", 0)

        return total_additional_power

    def get_additional_hp(self) -> int:
        if self.potion:
            return self.potion["effect"]["hp"]
        return 0

    def get_additional_protection(self) -> int:
        total_protection = 0
        for part_of_armour in self.armour:
            total_protection += part_of_armour["protection"]

        if self.potion:
            total_protection += self.potion["effect"].get("protection", 0)

        return total_protection

    def modify_knight(self) -> None:
        self.add_hp()
        self.add_power()
        self.add_protection()

    def get_hp(self) -> int:
        return self.hp

    def get_power(self) -> int:
        return self.power

    def get_protection(self) -> int:
        return self.protection
