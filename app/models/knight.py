from app.models.equipment import Weapon, Armour, Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = []
        self.weapon = None
        self.potion = None

    def equip_armor(self, armor_objects: list[Armour]) -> None:
        self.armour.extend(armor_objects)

    def equip_weapon(self, weapon : Weapon) -> None:
        self.weapon = weapon

    def equip_potion(self, potion: Potion) -> None:
        self.potion = potion

    def apply_potion_effects(self) -> None:
        if self.potion:
            effects = self.potion.effect
            if "power" in effects:
                self.power += effects["power"]
            if "hp" in effects:
                self.hp += effects["hp"]
            if "protection" in effects:
                self.protection += effects["protection"]

    def calculate_protection(self) -> None:
        self.protection = 0
        for armor in self.armour:
            self.protection += armor.protection

    def prepare_for_battle(self) -> None:
        if self.weapon:
            self.power += self.weapon.power
        self.calculate_protection()
        self.apply_potion_effects()

    def take_damage(self, damage: int) -> None:
        if damage > 0:
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0

    def is_alive(self) -> bool:
        return self.hp > 0
