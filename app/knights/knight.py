from __future__ import annotations


class Knight:
    def __init__(self, name: str,
                 health: int,
                 power: int,
                 armour: int,
                 weapon: dict,
                 potion: dict) -> None:
        self.name = name
        self.health = health
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @staticmethod
    def create_knight(info: dict) -> Knight | None:
        if not info["weapon"]:
            print("You can't fight without weapon")

        return Knight(info["name"],
                      info["hp"],
                      info["power"],
                      info["armour"],
                      info["weapon"],
                      info["potion"])

    def __str__(self) -> str:
        return (f"{self.name} "
                f"{self.health} "
                f"{self.power} "
                f"{self.armour} "
                f"{self.weapon} "
                f"{self.potion}")

    def __repr__(self) -> str:
        return (
            f"Knight(name={self.name!r}, "
            f"health={self.health}, "
            f"power={self.power}, "
            f"armour={self.armour}), "
            f"weapon={self.weapon}, "
            f"potion={self.potion})"
        )
