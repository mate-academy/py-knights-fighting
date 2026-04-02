from app.utils import sum_protection, apply_weapon
from app.utils import apply_potion


class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config.get("name", "Unknown")
        self.hp = config.get("hp", 100)
        self.base_power = config.get("power", 0)
        self.armour = config.get("armour") or []
        self.weapon = config.get("weapon")
        self.potion = config.get("potion")
        self.power = self.base_power
        self.protection = 0

    def prepare(self) -> None:
        self.protection = sum_protection(self.armour)
        self.power = apply_weapon(self.base_power, self.weapon)
        stats = {"hp": self.hp, "power": self.power,
                 "protection": self.protection}
        updated = apply_potion(stats, self.potion)

        self.hp = max(updated.get("hp", stats["hp"]), 0)
        self.power = updated.get("power", stats["power"])
        self.protection = updated.get("protection", stats["protection"])


def fight_once(attacker: Knight, defender: Knight) -> None:
    """Simulate one-on-one exchange of blows between a and b."""
    dmg_to_attacker = max(0, defender.power - attacker.protection)
    dmg_to_defender = max(0, attacker.power - defender.protection)

    attacker.hp = max(attacker.hp - dmg_to_attacker, 0)
    defender.hp = max(defender.hp - dmg_to_defender, 0)
