from app.preparations.armour import apply_armour
from app.preparations.potion import apply_potion
from app.preparations.power import apply_weapon


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict],
        weapon: dict,
        potion: None | dict,
        protection: int = 0,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def prepare_knight(self) -> None:
        apply_armour(self)
        apply_weapon(self)
        if self.potion is not None:
            apply_potion(self)
