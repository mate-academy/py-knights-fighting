from app.models.armour import Armour
from app.models.potion import Potion
from app.models.weapon import Weapon


class Knight:
    def __init__(
        self,
        name: str,
        hp: int,
        power: int,
        armour: list[Armour],
        weapon: Weapon,
        potion: Potion | None,
    ) -> None:
        self.name = name
        self.base_hp = hp
        self.base_power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @classmethod
    def from_dict(cls, knight_data: dict) -> "Knight":
        armour_objects = [
            Armour(item["part"], item["protection"])
            for item in knight_data["armour"]
        ]

        weapon_object = Weapon(
            knight_data["weapon"]["name"],
            knight_data["weapon"]["power"],
        )

        potion_data = knight_data["potion"]
        potion_object = None

        if potion_data is not None:
            potion_object = Potion(
                potion_data["name"],
                potion_data["effect"],
            )

        return cls(
            name=knight_data["name"],
            hp=knight_data["hp"],
            power=knight_data["power"],
            armour=armour_objects,
            weapon=weapon_object,
            potion=potion_object,
        )

    @property
    def total_protection(self) -> int:
        protection = 0

        for armour_item in self.armour:
            protection += armour_item.protection

        if self.potion is not None:
            protection += self.potion.effect.get("protection", 0)

        return protection

    @property
    def total_power(self) -> int:
        total = self.base_power + self.weapon.power

        if self.potion is not None:
            total += self.potion.effect.get("power", 0)

        return total

    @property
    def total_hp(self) -> int:
        total = self.base_hp

        if self.potion is not None:
            total += self.potion.effect.get("hp", 0)

        return total
