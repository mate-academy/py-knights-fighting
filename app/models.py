class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __repr__(self) -> str:
        return f"Armour(part={self.part}, protection={self.protection})"


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __repr__(self) -> str:
        return f"Weapon(name={self.name}, power={self.power})"


class Potion:
    def __init__(self, name: str, effect: int) -> None:
        self.name = name
        self.effect = effect

    def __repr__(self) -> str:
        return f"Potion(name={self.name}, effect={self.effect})"


class Knight:
    def __init__(self, name: str, base_power: int, hp: int,
                 armour: list = None, weapon: Weapon = None,
                 potion: Potion = None) -> None:
        self.name = name
        self.base_power = base_power
        self.hp = hp
        self.armour = armour if armour is not None else []
        self.weapon = weapon
        self.potion = potion
        self.power = self.base_power
        self.protection = sum(a.protection for a in self.armour)

    def apply_gear(self) -> None:
        if self.weapon:
            self.power += self.weapon.power
        if self.potion is not None:
            self.hp += self.potion.effect

    def __repr__(self) -> str:
        return (
            f"Knight(name={self.name}, base_power={self.base_power}, "
            f"hp={self.hp}, armour={self.armour}, "
            f"weapon={self.weapon}, potion={self.potion})"
        )
