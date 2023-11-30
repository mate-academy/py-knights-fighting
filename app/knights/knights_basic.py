class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        if self.potion is not None:
            for affects_on, value in self.potion["effect"].items():
                setattr(self, affects_on, getattr(self, affects_on) + value)

    def attack(self, other: "Knight") -> dict:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
        return {
            self.name: self.hp,
            other.name: other.hp,
        }
