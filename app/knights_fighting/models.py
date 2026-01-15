class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict = None,
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.power = self.base_power
        self.hp = self.base_hp
        self.protection = 0
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= max(0, damage)
        if self.hp < 0:
            self.hp = 0

    def fight(self, opponent: "Knight") -> None:
        self.take_damage(opponent.power - self.protection)
        opponent.take_damage(self.power - opponent.protection)

    def __repr__(self) -> str:
        return (f"Knight({self.name}, HP: {self.hp}, "
                f"Power: {self.power}, Protection: {self.protection})")
