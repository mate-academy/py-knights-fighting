from dataclasses import dataclass


@dataclass
class Effect:
    hp: int
    power: int
    protection: int

    @classmethod
    def create(cls, effect: dict) -> "Effect":
        hp = effect["hp"] if effect.get("hp") else 0
        power = effect["power"] if effect.get("power") else 0
        protection = effect["protection"] if effect.get("protection") else 0
        return cls(hp, power, protection)


@dataclass
class Potion:
    name: str
    effect: Effect

    @classmethod
    def create(cls, knight: dict) -> "Potion":
        if knight["potion"]:
            return cls(knight["potion"]["name"],
                       Effect.create(knight["potion"]["effect"]))
