class Knight:
    def __init__(
            self, knight: dict
    ) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = 0
        for protect in self.armour:
            self.protection += protect["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion_effect(self, effect_name: str, value: int) -> None:
        setattr(self, effect_name,
                getattr(self, effect_name) + value)

    def apply_potion(self) -> None:
        if self.potion is not None:
            for effect, value in self.potion["effect"].items():
                self.apply_potion_effect(effect, value)

    @staticmethod
    def battle_between_two(knight1: Knight, knight2: Knight) -> None:
        Knight.get_damage(knight1, knight2.power)
        Knight.get_damage(knight2, knight1.power)

    @staticmethod
    def get_damage(knight: Knight, damage: int) -> None:
        knight.hp -= damage - knight.protection
        if knight.hp < 0:
            knight.hp = 0
