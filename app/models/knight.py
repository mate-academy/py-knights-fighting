from app.models.armour import Armour
from app.models.potion import Potion
from app.models.weapon import Weapon


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[Armour],
        weapon: Weapon,
        potion: Potion | None = None,
    ) -> None:
        self.name: str = name
        self.base_power: int = power
        self.base_hp: int = hp
        self.armour: list[Armour] = armour
        self.weapon: Weapon = weapon
        self.potion: Potion | None = potion

        self.hp: int = self.base_hp
        self.power: int = self.base_power + self.weapon.power
        self.protection: int = sum(piece.protection for piece in self.armour)

        if self.potion:
            self.apply_potion_effect()

    def apply_potion_effect(self) -> None:
        if self.potion is None:
            return

        effects: dict[str, int] = self.potion.effect
        self.hp += effects.get("hp", 0)
        self.power += effects.get("power", 0)
        self.protection += effects.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        net_damage: int = max(0, damage - self.protection)
        self.hp = max(0, self.hp - net_damage)

    def __repr__(self) -> str:
        return (
            f"Knight(name={self.name}, power={self.power}, hp={self.hp}, "
            f"armour={self.armour}, weapon={self.weapon}, "
            f"potion={self.potion}, protection={self.protection})"
        )
