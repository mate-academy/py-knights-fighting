class Knight:
    def __init__(self, stats: dict) -> None:
        self.name = stats["name"]
        self.base_hp = stats["hp"]
        self.base_power = stats["power"]

        self.armour = stats.get("armour", [])
        self.weapon = stats.get("weapon")
        self.potion = stats.get("potion")

        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0

        self.apply_gear()

    def calculate_protection(self) -> int:
        total_protection = 0
        for armour in self.armour:
            total_protection += armour["protection"]
        return total_protection

    def apply_potion_effect(self) -> None:
        if self.potion and self.potion.get("effect"):
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.get("power", 0)

    def apply_gear(self) -> None:
        self.protection = self.calculate_protection()
        self.apply_weapon()
        self.apply_potion_effect()

    def attack(self, oponent: "Knight") -> None:
        damage = self.power - oponent.protection
        if damage > 0:
            oponent.hp -= damage
        if oponent.hp < 0:
            oponent.hp = 0

    def get_final_stats(self) -> dict:
        return {
            "name": self.name,
            "hp": self.hp,
        }
