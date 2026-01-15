class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict = None,
            protection: int = 0,

    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        self.protection = protection

        self.apply_armour()
        self.equip_weapon()
        self.use_potion()

    def apply_armour(self) -> int:
        for item in self.armour:
            self.protection += item["protection"]
        return self.protection

    def equip_weapon(self) -> int:
        self.power += self.weapon["power"]
        return self.power

    def use_potion(self) -> None:
        if self.potion is not None:
            for effect, value in self.potion["effect"].items():
                setattr(self, effect, getattr(self, effect) + value)

    def defend(self, opponent_attack: int) -> None:
        hp_after_attack = self.hp - (opponent_attack - self.protection)

        if hp_after_attack <= 0:
            self.hp = 0
        else:
            self.hp = hp_after_attack
