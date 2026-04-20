class Equipment:
    def __init__(self, armour: list | None,
                 weapon: dict | None, potion: dict | None) -> None:
        self.armour = list(armour) if armour else []
        self.weapon = weapon
        self.potion = potion

    def total_protection(self) -> int:
        return sum(int(part.get("protection", 0)) for part in self.armour)

    def apply_weapon(self, stats: dict) -> dict:
        new_stats = stats.copy()
        if self.weapon and isinstance(self.weapon, dict):
            new_stats["power"] =\
                (int(new_stats.get("power", 0))
                 + int(self.weapon.get("power", 0)))
        return new_stats

    def apply_potion(self, stats: dict) -> dict:
        new_stats = stats.copy()
        if self.potion and isinstance(self.potion, dict):
            effect = self.potion.get("effect") or {}
            if isinstance(effect, dict):
                for key in ("hp", "power", "protection"):
                    delta = int(effect.get(key, 0))
                    if delta:
                        new_stats[key] = int(new_stats.get(key, 0)) + delta
        return new_stats
