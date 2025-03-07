from __future__ import annotations


class KnightsStats:
    def __init__(self, stats: dict) -> None:
        self.stats = stats

    def apply_equipments(self) -> KnightsStats:
        self.stats["protection"] = 0
        for armour in self.stats["armour"]:
            self.stats["protection"] += armour["protection"]

        self.stats["power"] += self.stats["weapon"]["power"]

        if self.stats["potion"]:
            for effect_name, effect in self.stats["potion"]["effect"].items():
                self.stats[effect_name] += effect

        return self
