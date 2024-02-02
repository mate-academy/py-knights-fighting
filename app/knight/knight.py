from app.knight_equipment.armour import Armour
from app.knight_equipment.potion import Potion
from app.knight_equipment.weapon import Weapon


class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.armour = [
            Armour(
                part=armour_part["part"],
                protection=armour_part["protection"]
            )
            for armour_part in knight_config["armour"]
        ]

        self.weapon = Weapon(
            name=knight_config["weapon"]["name"],
            power=knight_config["weapon"]["power"]
        )

        self.potion = Potion(
            name=knight_config["potion"]["name"],
            effect=knight_config["potion"]["effect"]
        ) if knight_config.get("potion") else None

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
