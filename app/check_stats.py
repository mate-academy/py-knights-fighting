class Knight:

    def __init__(self, knights: dict) -> None:
        self.knights = knights
        self.name = knights["name"]
        self.power = knights["power"]
        self.hp = knights["hp"]

    def check_weapon(self) -> None:
        # check weapon
        if self.knights["weapon"]:
            self.power += self.knights["weapon"]["power"]

    def check_armour(self) -> None:
        # check armour
        if self.knights["armour"]:
            self.hp += sum(part["protection"] for part
                           in self.knights["armour"])

    def check_potion(self) -> None:
        # check potion
        if self.knights["potion"] is not None:
            potion_effect = self.knights["potion"]["effect"]
            # if potion_hp, + on base hp
            if "hp" in potion_effect:
                self.hp += potion_effect["hp"]
            # if potion_power, + on base power
            if "power" in potion_effect:
                self.power += potion_effect["power"]
            # if potion_protection, + on base hp
            if "protection" in potion_effect:
                self.hp += potion_effect["protection"]


class Battle:

    @staticmethod
    def battle_knight(knight1: "Knight", knight2: "Knight") -> tuple:
        knight1.hp -= knight2.power
        knight2.hp -= knight1.power
        if knight1.hp <= 0:
            knight1.hp = 0
        if knight2.hp <= 0:
            knight2.hp = 0
        return knight1.hp, knight2.hp
