from app.entities import Weapon, Potion


class Knight:
    def __init__(
        self,
        name: str,
        base_power: int,
        hp: int,
        armour: list,
        weapon: Weapon,
        potion: Potion = None,
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.power = self.calculate_power()
        self.protection = self.calculate_protection()
        self.hp = self.calculate_total_hp()

    def calculate_power(self) -> int:
        total_power = self.base_power + self.weapon.power
        if self.potion and "power" in self.potion.effect:
            total_power += self.potion.effect["power"]
        return total_power

    def calculate_protection(self) -> int:
        total_protection = sum(arm.protection for arm in self.armour)
        if self.potion and "protection" in self.potion.effect:
            total_protection += self.potion.effect.get("protection", 0)
        return total_protection

    def calculate_total_hp(self) -> int:
        total_hp = self.hp
        if self.potion and "hp" in self.potion.effect:
            total_hp += self.potion.effect["hp"]
        return total_hp

    def take_damage(self, damage: int) -> None:
        self.hp = max(0, self.hp - damage)

    def is_defeated(self) -> bool:
        return self.hp == 0
