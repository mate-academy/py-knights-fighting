from app.aquipment.armor import Armor
from app.aquipment.weapon import Weapon
from app.aquipment.potion import Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict) -> None:
        self.protection = 0
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armor(a["part"], a["protection"]) for a in armour]
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.potion = Potion(potion["name"],
                             potion["effect"]
                             ) if potion else None

    def apply_weapon(self) -> None:

        self.power += self.weapon.power

    def apply_armour(self) -> None:

        final_protect = 0
        for arm in self.armour:
            final_protect += arm.protection

        self.protection += final_protect

    def apply_potion(self) -> None:
        if self.potion:
            self.power += self.potion.effect.get("power", 0)
            self.hp += self.potion.effect.get("hp", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def prepare_to_battle(self) -> None:
        self.apply_weapon()
        self.apply_armour()
        self.apply_potion()

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
