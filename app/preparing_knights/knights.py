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

    # for recalculating stats before the fights
    @staticmethod
    def apply_knights() -> None:
        for name, instance in Knights.knights_inst.items():
            # calculating 'protection' on base of armour's stats:
            if instance.armour:
                instance.protection += sum(
                    [armour.protection for armour in instance.armour]
                )
            # recalculating 'power' on base of weapon's stat:
            instance.power += instance.weapon.power
            # recalculating all stats on base of potion's stats:
            if instance.potion:
                if instance.potion.effect.get("power"):
                    instance.power += instance.potion.effect.get("power")
                if instance.potion.effect.get("hp"):
                    instance.hp += instance.potion.effect.get("hp")
                if instance.potion.effect.get("protection"):
                    instance.protection += instance.potion.effect.get(
                        "protection"
                    )

    # for recalculating 'hp' after the fights:
    @staticmethod
    def recount_hp() -> None:
        for name, instance in Knights.knights_inst.items():
            if instance.hp < 0:
                instance.hp = 0
