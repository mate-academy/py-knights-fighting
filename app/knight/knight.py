from app.items import Armor, Weapon, Potion


class Knight:

    def __init__(self, name: str, power: int, hp: int, armour : Armor,
                 weapon: Weapon, potion: Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        self.protection = sum(a.protection for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion.effect
            if "power" in effect.keys():
                self.power += effect["power"]
            if "protection" in effect.keys():
                self.protection += effect["protection"]
            if "hp" in effect.keys():
                self.hp += effect["hp"]

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def receive_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
