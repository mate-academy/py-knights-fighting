from typing import Optional


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name: str = name
        self.power: int = power


class Armor:
    def __init__(self, part: str, protection: int) -> None:
        self.part: str = part
        self.protection: int = protection


class Potion:
    def __init__(self, name: str, effect: dict[str, int]) -> None:
        self.name: str = name
        self.effect: dict[str, int] = effect


class Knight:
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]
        self.base_hp: int = config["hp"]
        self.base_power: int = config["power"]
        self.armor: list[Armor] = [
            Armor(**a) for a in config.get("armour", [])
        ]
        self.weapon: Weapon = Weapon(**config["weapon"])
        potion_cfg: Optional[dict] = config.get("potion")
        self.potion: Optional[Potion] = (
            Potion(**potion_cfg)) if potion_cfg else None

        self.hp: int = self.base_hp
        self.power: int = self.base_power
        self.protection: int = 0

    def apply_gear(self) -> None:
        self.power += self.weapon.power
        self.protection = sum(a.protection for a in self.armor)

        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def attack(self, opponent: "Knight") -> None:
        damage: int = max(self.power - opponent.protection, 0)
        opponent.hp = max(opponent.hp - damage, 0)
