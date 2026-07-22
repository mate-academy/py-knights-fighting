from dataclasses import dataclass

from app.stats import calculate_effective_stats


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    protection: int

    @classmethod
    def from_config(cls, config: dict) -> "Knight":
        stats = calculate_effective_stats(config)
        return cls(**stats)

    def take_damage(self, incoming_power: int) -> None:
        self.hp = max(0, self.hp - (incoming_power - self.protection))

    def fight(self, opponent: "Knight") -> None:
        self_power = self.power
        self.take_damage(opponent.power)
        opponent.take_damage(self_power)
