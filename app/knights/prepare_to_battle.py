from app.knights.basic_stats import Knight


class KnightsPrepareToBattle:

    def __init__(self, knight: Knight) -> None:
        self.name = knight.name
        self.power = knight.power
        self.hp = knight.hp
        self.protection = 0

    def apply_armour(self, knight: Knight) -> None:
        for element in knight.armour:
            self.protection += element["protection"]

    def apply_weapon(self, knight: Knight) -> None:
        self.power += knight.weapon["power"]

    def apply_potion(self, knight: Knight) -> None:
        if knight.potion is not None:
            for potion_effect in knight.potion["effect"]:
                setattr(self, potion_effect,
                        getattr(self, potion_effect)
                        + knight.potion["effect"][potion_effect])

    def check_hp_after_battle(self) -> None:
        if self.hp < 0:
            self.hp = 0
