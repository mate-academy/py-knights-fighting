from app.equipment import Armour, Weapon, Potion


class Knight:
    def __init__(self, knight_stats: dict):
        self.knight_stats = knight_stats
        self.name = knight_stats["name"]
        self.hp = knight_stats["hp"]
        self.power = knight_stats["power"]
        self.protection = 0

    def prepare_to_battle(self) -> None:
        armour = Armour(self.knight_stats["armour"])
        self.protection += armour.apply_armor()

        weapon = Weapon(self.knight_stats["weapon"])
        self.power += weapon.get_power()

        potion = Potion(self.knight_stats["potion"])
        potion.apply_potion(self)

    def attack_enemy(self, other) -> None:
        other.hp -= self.power - other.protection

    def hp_check(self) -> None:
        if self.hp <= 0:
            self.hp = 0
