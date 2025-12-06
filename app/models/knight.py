from .armour import Armour
from .weapon import Weapon
from .potion import Potion


class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.base_hp = config["hp"]
        self.hp = config["hp"]

        self.base_power = config["power"]
        self.power = config["power"]

        self.armour_parts = [Armour(a["part"], a["protection"]) for a in config.get("armour", [])]
        self.protection = 0

        weapon_cfg = config.get("weapon")
        self.weapon = Weapon(weapon_cfg["name"], weapon_cfg["power"])

        potion_cfg = config.get("potion")
        self.potion = Potion(potion_cfg["name"], potion_cfg["effect"]) if potion_cfg else None

    # ---------------------------------------------------------

    def apply_armour(self) -> None:
        self.protection = sum(part.protection for part in self.armour_parts)

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if not self.potion:
            return

        effect = self.potion.effect
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)

    # ---------------------------------------------------------

    def prepare(self) -> None:
        """Apply armour, weapon and potion effects."""
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    # ---------------------------------------------------------

    def take_damage(self, amount: int) -> None:
        self.hp -= max(amount, 0)
        if self.hp < 0:
            self.hp = 0
