from __future__ import annotations


class KnightStats:

    def __init__(self, stats: dict) -> None:
        self.stats = stats

    def potion_effect(self) -> None:
        # Check out this potion
        if "power" in self.stats["potion"]["effect"]:
            self.stats["power"] += self.stats["potion"]["effect"]["power"]

        if "protection" in self.stats["potion"]["effect"]:
            self.stats["protection"] += (
                self.stats)["potion"]["effect"]["protection"]

        if "hp" in self.stats["potion"]["effect"]:
            self.stats["hp"] += self.stats["potion"]["effect"]["hp"]

    def final_stats(self) -> dict:
        # Statistics at the time of the fight
        self.stats["protection"] = 0

        if self.stats["potion"] is not None:
            self.potion_effect()

        for part in self.stats["armour"]:
            self.stats["protection"] += part["protection"]

        self.stats["power"] += self.stats["weapon"]["power"]
        return self.stats
