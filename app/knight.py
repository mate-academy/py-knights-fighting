class Armour:
    def __init__(
        self,
        part: str,
        protection: int,
    ) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(
        self,
        name: str,
        power: int,
    ) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(
        self,
        name: str,
        effect: dict,
    ) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[Armour],
        weapon: Weapon,
        potion: Potion | None
    ) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = [Armour(a["part"], a["protection"]) for a in armour]
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.potion = (
            Potion(potion["name"], potion["effect"])
            if potion is not None
            else None
        )
        self.protection = 0
        self.power = 0
        self.prepare_knight()

    def prepare_knight(self) -> None:
        # apply armour
        self.protection = sum(item.protection for item in self.armour)
        # apply weapon
        self.power = self.base_power + self.weapon.power
        # apply potion
        if self.potion is not None:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]
            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]
            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]

    def fight(self, opponent: "Knight") -> None:
        damage_taken = opponent.power - self.protection
        self.hp -= damage_taken if damage_taken > 0 else 0
        if self.hp <= 0:
            self.hp = 0
