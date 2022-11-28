from __future__ import annotations


class Knight:
    def __init__(self, stats_and_equipment: dict) -> None:
        self.name: str = stats_and_equipment["name"]
        self.power: int = stats_and_equipment["power"]
        self.hp: int = stats_and_equipment["hp"]
        self.armour: list[dict] = stats_and_equipment["armour"]
        self.weapon: dict = stats_and_equipment["weapon"]
        self.potion: dict | None = stats_and_equipment["potion"]
        self.protection: int = 0

        self.apply_stats_of_armour()
        self.apply_stats_of_weapon()
        self.apply_stats_of_potion()

    def apply_stats_of_armour(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]

    def apply_stats_of_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_stats_of_potion(self) -> None:
        if self.potion is not None:
            stats = ["hp", "power", "protection"]

            for stat in stats:
                if stat in self.potion["effect"]:
                    old_value_of_stat = getattr(self, stat)

                    new_value_of_stat = (old_value_of_stat
                                         + self.potion["effect"][stat])

                    setattr(self, stat, new_value_of_stat)

    def fight(self, other_knight: Knight) -> None:
        self.hp += min(self.protection - other_knight.power, 0)
        other_knight.hp += min(other_knight.protection - self.power, 0)

        self.hp = max(self.hp, 0)
        other_knight.hp = max(other_knight.hp, 0)
