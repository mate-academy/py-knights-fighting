class Knight:
    def __init__(self, name: str, power: int, hp: int, protection: int = 0, armour=None, weapon=None, potion=None):
        self.name = name
        self.base_power = power
        self.hp = hp
        self.protection = protection
        self.armour = armour if armour is not None else []
        self.weapon = weapon
        self.potion = potion

        self.power = self.calculate_total_power()


    def calculate_protection(self):
        return sum(a['protection'] for a in self.armour)

    def calculate_total_power(self):

        total_power = self.base_power
        if self.weapon:
            total_power += self.weapon['power']
        if self.potion and 'power' in self.potion.get('effect', {}):
            total_power += self.potion['effect']['power']
        return total_power

    @property
    def effective_power(self):
        return self.power

    @property
    def effective_hp(self):
        return self.hp

    def take_damage(self, damage: int):
        actual_damage = max(0, damage - self.protection)
        self.hp -= actual_damage
        print(f"{self.name} takes {actual_damage} damage and has {self.hp} HP left.")

    def calculate_stats(self):
        return {
            'name': self.name,
            'base_power': self.base_power,
            'total_power': self.power,
            'hp': self.hp,
            'protection': self.protection,
            'weapon': self.weapon['name'] if self.weapon else None,
            'potion': self.potion['name'] if self.potion else None
        }

    def __repr__(self):
        return (f"Knight(name={self.name}, base_power={self.base_power}, "
                f"total_power={self.power}, hp={self.hp}, protection={self.protection})")
