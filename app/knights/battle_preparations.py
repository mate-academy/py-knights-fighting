from __future__ import annotations


class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.protection = sum([a["protection"] for a in knight["armour"]])
        self.power = knight["power"] + knight["weapon"]["power"]
        self.hp = knight["hp"]

    def __repr__(self) -> str:
        return f"{self.hp}"

    def apply_potion(self, knight: dict) -> Knight:
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                self.power += knight["potion"]["effect"]["power"]
            if "protection" in knight["potion"]["effect"]:
                self.protection += knight["potion"]["effect"]["protection"]
            if "hp" in knight["potion"]["effect"]:
                self.hp += knight["potion"]["effect"]["hp"]
        return self
