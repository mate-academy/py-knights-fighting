from app.knights.armor import ArmourPart
from app.knights.potion import Potion, PotionEffect
from app.knights.weapon import Weapon


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict = None
                 ) -> None:
        self.total_hp = 0
        self.total_power = 0
        self.total_protection = 0
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [ArmourPart(**part) for part in armour]
        self.weapon = Weapon(**weapon)
        self.potion = Potion(potion["name"],
                             PotionEffect(**potion["effect"]
                                          )) if potion else None

    def calculate_total_power(self) -> int:
        total_power = self.power + self.weapon.power

        # I add strength from the potion, if there is one
        if self.potion and hasattr(self.potion.effect, "power"):
            total_power += self.potion.effect.power

        return total_power

    def calculate_total_hp(self) -> int:
        total_protection = sum(part.protection for part in self.armour)
        total_hp = self.hp + total_protection

        # I add the effect of the potion, if there is one
        if self.potion:
            if hasattr(self.potion.effect, "hp"):
                total_hp += self.potion.effect.hp
            if hasattr(self.potion.effect, "protection"):
                total_hp += self.potion.effect.protection

        return total_hp

    def prepare_for_battle(self) -> None:
        # Calculates total protection
        self.total_protection = sum(part.protection for part in self.armour)

        # Calculates total power
        self.total_power = self.power + self.weapon.power
        if self.potion and hasattr(self.potion.effect, "power"):
            self.total_power += self.potion.effect.power

        # Calculates total hp
        self.total_hp = self.hp + self.total_protection
        if self.potion:
            if hasattr(self.potion.effect, "hp"):
                self.total_hp += self.potion.effect.hp
            if hasattr(self.potion.effect, "protection"):
                self.total_hp += self.potion.effect.protection

    def __repr__(self) -> str:
        return (f"Knight(name={self.name}, "
                f" power={self.power}, "
                f" hp={self.hp}, "
                f" armour={self.armour}, "
                f" weapon={self.weapon}, "
                f" potion={self.potion}, "
                f" total_protection={self.total_protection}, "
                f" total_hp={self.total_hp}, "
                f" total_power={self.total_power})")
