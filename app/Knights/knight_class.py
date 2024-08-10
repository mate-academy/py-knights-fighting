from __future__ import annotations


class Knight:
    def __init__(self, parameters: dict) -> None:
        self.name = parameters["name"]
        self.hp = parameters["hp"]
        self.protection = sum(
            armour["protection"] for armour in parameters["armour"]
        )
        self.power = parameters["power"] + parameters["weapon"]["power"]

        if parameters["potion"] is not None:
            self.power += parameters["potion"]["effect"].get("power", 0)
            self.protection += (
                parameters["potion"]["effect"].get("protection", 0)
            )
            self.hp += parameters["potion"]["effect"].get("hp", 0)

    def knights_buttle(self, other: Knight) -> None:
        self.hp = max(0, self.hp - (other.power - self.protection))
        other.hp = max(0, other.hp - (self.power - other.protection))
