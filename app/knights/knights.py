from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


class Knight:

    def __init__(self, base_equip: dict) -> None:
        self.name = base_equip.get("name")
        self.base_power = base_equip.get("power")
        self.base_hp = base_equip.get("hp")
        self.protection = 0
        self.armour = []
        self.weapon = {}
        self.potion = {}

        for equip in base_equip:

            if equip == "armour" and base_equip.get(equip):
                for part in base_equip.get(equip):
                    Armour(part["part"], part["protection"])
                    self.protection += part["protection"]
                    self.armour.append(Armour)

            if equip == "weapon":
                Weapon(
                    base_equip.get(equip)["name"],
                    base_equip.get(equip)["power"]
                )
                self.base_power += base_equip.get(equip)["power"]

            if equip == "potion" and base_equip.get(equip):
                Potion(
                    base_equip.get(equip)["name"],
                    base_equip.get(equip)["effect"]
                )

                for stat, option in base_equip.get(equip)["effect"].items():
                    if stat == "power":
                        setattr(
                            self,
                            "base_power",
                            getattr(self, "base_power", 0) + option
                        )
                    elif stat == "hp":
                        setattr(
                            self,
                            "base_hp",
                            getattr(self, "base_hp", 0) + option
                        )
                    elif stat == "protection":
                        setattr(
                            self,
                            "protection",
                            getattr(self, "protection", 0) + option
                        )

    def return_properties(self) -> dict:
        return {"name": self.name,
                "hp": self.base_hp,
                "power": self.base_power,
                "protection": self.protection}
