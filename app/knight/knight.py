from app.knight_equipment.armour import Armour
from app.knight_equipment.potion import Potion
from app.knight_equipment.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [
            Armour(**armour_part)
            for armour_part in armour
        ]

        self.weapon = Weapon(**weapon)
        self.potion = Potion(**potion) if potion else None
        self.protection = 0

        self.prepare_to_battle()

    def prepare_to_battle(self) -> None:
        self.apply_armor()
        self.apply_weapon()
        self.apply_potion()

    def apply_armor(self) -> None:
        for armor_item in self.armour:
            self.protection += armor_item.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            if self.potion.effect.get("power"):
                self.power += self.potion.effect["power"]

            if self.potion.effect.get("hp"):
                self.hp += self.potion.effect["hp"]

            if self.potion.effect.get("protection"):
                self.protection += self.potion.effect["protection"]

    def receive_damage(self, attacker_power: int) -> None:
        total_damage = attacker_power - self.protection

        self.hp -= total_damage

        if self.hp < 0:
            self.hp = 0
