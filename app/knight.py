from __future__ import annotations


class Knight:
    """Represents a knight with stats, armour, weapon and potion."""

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict] | None = None,
        weapon: dict | None = None,
        potion: dict | None = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self._armour = armour or []
        self._weapon = weapon
        self._potion = potion

    @classmethod
    def from_dict(cls, config: dict) -> Knight:
        """Create a Knight instance from a dictionary config."""
        knight = cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config.get("armour"),
            weapon=config.get("weapon"),
            potion=config.get("potion"),
        )
        knight.prepare_for_battle()
        return knight

    def prepare_for_battle(self) -> None:
        """Apply armour, weapon and potion effects before battle."""
        self._apply_armour()
        self._apply_weapon()
        self._apply_potion()

    def _apply_armour(self) -> None:
        """Calculate total protection from all armour pieces."""
        for piece in self._armour:
            self.protection += piece["protection"]

    def _apply_weapon(self) -> None:
        """Add weapon power to knight's base power."""
        if self._weapon:
            self.power += self._weapon["power"]

    def _apply_potion(self) -> None:
        """Apply potion effects to knight's stats."""
        if self._potion is None:
            return

        effect = self._potion.get("effect", {})
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)

    def take_damage(self, attacker_power: int) -> None:
        """Calculate damage taken based on attacker power and protection."""
        damage = attacker_power - self.protection
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0


def fight(knight1: Knight, knight2: Knight) -> None:
    """Execute a battle between two knights (simultaneous attack)."""
    knight1_power = knight1.power
    knight2_power = knight2.power

    knight1.take_damage(knight2_power)
    knight2.take_damage(knight1_power)
