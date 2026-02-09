from app.equip_for_warriors.armour import Armour
from app.equip_for_warriors.potion import Potion
from app.equip_for_warriors.weapon import Weapon
from app.knights.warrior import Warrior


class Knight:

    def __init__(self, warrior: Warrior, armors: list[Armour],
                 weapon: Weapon, potion: Potion = None) -> None:

        self.armors = armors
        self.weapon = weapon
        self.potion = potion

        self.stats = self.calculate_stats(warrior, armors, weapon, potion)

        self.name = warrior.name
        self.hp = self.stats['hp']
        self.power = self.stats['power']
        self.protection = self.stats['protection']

    def __str__(self):
        return (f"{self.name} stats: hp={self.hp}, power={self.power}, "
              f"protection={self.protection}")

    @staticmethod
    def calculate_stats(warrior: Warrior, armors: list[Armour], weapon: Weapon,
                        potion: Potion = None) -> dict:
        stats = dict(hp=warrior.hp, power=warrior.power, protection=0)
        stats['protection'] += sum(armour.protection for armour in armors)
        stats["power"] += weapon.power
        if potion:
            for key, value in potion.effects.items():
                stats[key] += value

        return stats
