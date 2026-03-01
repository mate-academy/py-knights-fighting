from dataclasses import dataclass


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __repr__(self) -> str:
        return f'Weapon(name: "{self.name}", power: {self.power})'

    @classmethod
    def from_dict(cls, data: dict) -> "Weapon":
        return cls(name=data["name"], power=data["power"])


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __repr__(self) -> str:
        return f"Armour(part: '{self.part}', protection: {self.protection})"

    @classmethod
    def from_dict(cls, data: dict) -> "Armour":

        return cls(part=data["part"], protection=data["protection"])


@dataclass
class Effect:
    power: int = 0
    hp: int = 0
    protection: int = 0

    @classmethod
    def from_dict(cls, data: dict) -> "Effect":
        return cls(
            power=data.get("power", 0),
            hp=data.get("hp", 0),
            protection=data.get("protection", 0),
        )


@dataclass
class Potion:
    name: str
    effect: Effect

    @classmethod
    def from_dict(cls, data: dict | None) -> "Potion | None":
        if data is None:
            return None
        return cls(
            name=data["name"],
            effect=Effect.from_dict(data.get("effect", {})),
        )


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: Weapon,
        armour: list[Armour],
        potion: Potion | None = None,
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion

    def __repr__(self) -> str:
        return f"name: {self.name}"

    @classmethod
    def from_dict(cls, data: dict) -> "Knight":
        weapon = Weapon.from_dict(data["weapon"])

        armour = [Armour.from_dict(a) for a in (data.get("armour") or [])]

        potion = Potion.from_dict(data.get("potion"))

        return cls(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            weapon=weapon,
            armour=armour,
            potion=potion,
        )

    def get_protection(self) -> int:
        protection = sum(a.protection for a in (self.armour or []))
        if self.potion:
            protection += self.potion.effect.protection
        return protection

    def get_power(self) -> int:
        power = self.power + self.weapon.power
        if self.potion:
            power += self.potion.effect.power
        return power

    def get_hp(self) -> int:
        hp = self.hp
        if self.potion:
            hp += self.potion.effect.hp
        return hp
