from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = (power + weapon["power"] +
                      (potion["effect"]["power"]
                       if potion and "power" in potion["effect"] else 0))
        self.hp = (hp +
                   (potion["effect"]["hp"]
                    if potion and "hp" in potion["effect"] else 0))
        self.protection = (
            sum(part["protection"] for part in armour) if armour else 0 +
            (potion["effect"].get("protection", 0) if potion else 0))

    @classmethod
    def config_optimize(cls, config: dict) -> Knight:
        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"]
        )
