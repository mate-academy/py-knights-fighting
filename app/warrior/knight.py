from dataclasses import dataclass, field

from app.warrior.utils.armour import Armour
from app.warrior.utils.weapon import Weapon
from app.warrior.utils.potion import Potion
from app.warrior.utils.potion import Effect


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: list[Armour]
    weapon: Weapon
    potion: Potion | None
    protection: int = field(init=False)

    def __post_init__(self) -> None:
        self.protection = 0
        self.armour = self.armour or []
        self._set_up()

    def _set_up(self) -> None:
        if self.potion is not None:
            self._use_potion()
        self._use_armour()
        self._use_weapon()

    def get_stats(self) -> tuple:
        return self.hp, self.power, self.protection

    def _use_potion(self) -> None:
        if self.potion is None:
            return
        self.hp += self.potion.effect.hp
        self.protection += self.potion.effect.protection
        self.power += self.potion.effect.power

    def _use_armour(self) -> None:
        for arm in self.armour:
            self.protection += arm.protection

    def _use_weapon(self) -> None:
        self.power += self.weapon.power

    @classmethod
    def from_dict(cls, data: dict) -> dict[str, Knight]:
        knights = {}
        for entry in data.values():
            name = entry.get("name")
            power = entry.get("power", 0)
            hp = entry.get("hp", 0)
            armour = cls._parse_armour(entry.get("armour", []))
            weapon = cls._parse_weapon(entry.get("weapon", {}))
            potion = cls._parse_potion(entry.get("potion"))
            knight = Knight(
                name=name,
                power=power,
                hp=hp,
                armour=armour,
                weapon=weapon,
                potion=potion
            )
            knights[name] = knight

        return knights

    @staticmethod
    def _parse_armour(data: list) -> list[Armour]:
        armour = []
        for entry in data:
            part = entry.get("part")
            protection = entry.get("protection", 0)
            armour.append(Armour(part, protection))
        return armour

    @staticmethod
    def _parse_weapon(data: dict) -> Weapon:
        name = data.get("name")
        power = data.get("power", 0)
        return Weapon(name, power)

    @staticmethod
    def _parse_potion(data: dict) -> Potion | None:
        if data is None:
            return None

        name = data.get("name")
        effect = data.get("effect", {})
        effect = Effect(
            effect.get("hp", 0),
            effect.get("power", 0),
            effect.get("protection", 0)
        )
        return Potion(name, effect)
