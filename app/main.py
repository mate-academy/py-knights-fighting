# app/knights.py
class Knight:
    def __init__(self, name, power, hp, armor, weapon, potion):
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion

    def calculate_stats(self):
        stats = {
            "hp": self.base_hp,
            "power": self.base_power,
            "protection": 0,
        }

        # Apply armor
        for armor_piece in self.armor:
            stats["protection"] += armor_piece.protection

        # Apply weapon
        stats["power"] += self.weapon.power

        # Apply potion if exists
        if self.potion:
            for effect_type, value in self.potion.effect.items():
                stats[effect_type] += value

        return stats


# app/weapons.py
class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power


# app/armor.py
class Armor:
    def __init__(self, part, protection):
        self.part = part
        self.protection = protection


# app/potions.py
class Potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


# app/battle.py
def battle(knight1, knight2):
    # Get stats before battle
    knight1_stats = knight1.calculate_stats()
    knight2_stats = knight2.calculate_stats()

    # BATTLE:

    # 1st knight attacks 2nd knight
    knight2_stats["hp"] -= max(0, knight1_stats["power"] - knight2_stats["protection"])

    # 2nd knight attacks 1st knight
    knight1_stats["hp"] -= max(0, knight2_stats["power"] - knight1_stats["protection"])

    # Check if someone fell in battle
    knight1_stats["hp"] = max(0, knight1_stats["hp"])
    knight2_stats["hp"] = max(0, knight2_stats["hp"])

    # Return battle results:
    return {knight1.name: knight1_stats["hp"], knight2.name: knight2_stats["hp"]}
