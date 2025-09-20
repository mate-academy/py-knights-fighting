from app.knights.weapon import Weapon
from app.knights.armour import Armour
from app.knights.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        hp: int,
        power: int,
        weapon: Weapon,
        armour: list[Armour] | None = None,
        potion: Potion | None = None,
    ) -> None:
        self.name = name
        self.base_hp = hp
        self.base_power = power
        self.weapon = weapon
        self.armour = armour or []
        self.potion = potion
        self.hp, self.power, self.protection = self._prepare_stats()

    def _prepare_stats(self) -> tuple[int, int, int]:
        hp = self.base_hp
        power = self.base_power
        protection = sum(a.protection for a in self.armour)

        power += self.weapon.power

        if self.potion:
            hp += self.potion.effect.get("hp", 0)
            power += self.potion.effect.get("power", 0)
            protection += self.potion.effect.get("protection", 0)

        return hp, power, protection

    def take_damage(self, enemy_power: int) -> None:
        damage = max(0, enemy_power - self.protection)
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
