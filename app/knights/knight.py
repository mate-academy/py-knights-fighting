class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict[str, int | str]],
            weapon: dict[str, int | str],
            potion: dict | None = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]
        self.power += self.weapon["power"]
        if self.potion is not None:
            for stat, value in self.potion["effect"].items():
                current_value = getattr(self, stat)
                setattr(self, stat, current_value + value)

    def take_damage(self, damage: int) -> None:
        if damage > 0:
            self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
