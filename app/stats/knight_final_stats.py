from __future__ import annotations


class KnightStats:

    def __init__(self, stats: dict) -> None:
        self.stats = stats

    def potion_effect(self) -> None:
        # Check out this potion
        for eff in self.stats["potion"]["effect"]:
            self.stats[eff] += self.stats["potion"]["effect"][eff]

    def final_stats(self) -> dict:
        # Statistics at the time of the fight
        self.stats["protection"] = 0

        if self.stats["potion"] is not None:
            self.potion_effect()

        for part in self.stats["armour"]:
            self.stats["protection"] += part["protection"]

        self.stats["power"] += self.stats["weapon"]["power"]
        return self.stats
