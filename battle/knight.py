from dataclasses import dataclass


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: list[dict] | None
    weapon: dict
    potion: dict | None

    @property
    def stats(self) -> dict:
        final_hp = self.hp
        final_protection = sum(
            a["protection"] for a in self.armour
        ) if self.armour else 0
        final_power = self.weapon["power"] + self.power

        if self.potion:
            effect = self.potion.get("effect", {})
            final_power += effect.get("power", 0)
            final_protection += effect.get("protection", 0)
            final_hp += effect.get("hp", 0)

        result = {
            "name": self.name,
            "power": final_power,
            "hp": final_hp,
            "protection": final_protection
        }

        return result

    def perform_battle(self, other: "Knight") -> None:
        k1_stats = self.stats
        k2_stats = other.stats

        self.hp = max(
            k1_stats["hp"] - (k2_stats["power"] - k1_stats["protection"]), 0
        )
        other.hp = max(
            k2_stats["hp"] - (k1_stats["power"] - k2_stats["protection"]), 0
        )

    @classmethod
    def from_dict(cls, data: dict) -> "Knight":
        return cls(**data)
