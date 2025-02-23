from __future__ import annotations


class Knight:

    def __init__(self, stats: dict) -> None:
        self.name = stats.get("name")
        self.hp = stats.get("hp")
        self.power = stats.get("power")

        # apply armour
        self.protection = 0
        for arm in stats.get("armour"):
            self.protection += arm.get("protection")

        # apply weapon
        self.power += stats.get("weapon").get("power")

        # apply potion if exist
        if stats.get("potion") is not None:
            potion_effect = stats.get("potion").get("effect")

            if "power" in potion_effect:
                self.power += potion_effect.get("power")

            if "protection" in potion_effect:
                self.protection += potion_effect.get("protection")

            if "hp" in potion_effect:
                self.hp += potion_effect.get("hp")

    def correct_stats(self) -> None:
        if self.hp <= 0:
            self.hp = 0
