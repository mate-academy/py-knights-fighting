from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knights:
    knights_inst = {}

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
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.knights_inst[self.name] = self

    @staticmethod
    def apply_knights() -> None:
        for name, instance in Knights.knights_inst.items():

            if instance.armour:
                instance.protection += sum(
                    [armour.protection for armour in instance.armour]
                )

            instance.power += instance.weapon.power

            if instance.potion:
                if instance.potion.effect.get("power"):
                    instance.power += instance.potion.effect.get("power")
                if instance.potion.effect.get("hp"):
                    instance.hp += instance.potion.effect.get("hp")
                if instance.potion.effect.get("protection"):
                    instance.protection += instance.potion.effect.get(
                        "protection"
                    )

    @staticmethod
    def recount_hp() -> None:
        for name, instance in Knights.knights_inst.items():
            if instance.hp < 0:
                instance.hp = 0
