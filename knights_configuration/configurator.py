from copy import deepcopy


class Configurator:
    def __init__(self, knights: dict) -> None:
        self.knights = deepcopy(knights)
        for knight_name in self.knights:
            self._prepare_knight(knight_name)

    def _prepare_knight(self, name: str) -> None:
        knight = self.knights[name]
        knight["protection"] = \
            sum(armour["protection"] for armour in knight["armour"])
        knight["power"] += knight["weapon"]["power"]
        if knight["potion"]:
            if "power" in knight["potion"]["effect"]:
                knight["power"] += \
                    knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                knight["protection"] += \
                    knight["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                knight["hp"] += knight["potion"]["effect"]["hp"]

    @staticmethod
    def _one_battle(knight1: dict, knight2: dict):
        knight1["hp"] -= knight2["power"] - knight1["protection"]
        knight2["hp"] -= knight1["power"] - knight2["protection"]

        knight1["hp"] = max(knight1["hp"], 0)
        knight2["hp"] = max(knight2["hp"], 0)

    def battle(self) -> dict:
        self._one_battle(self.knights["lancelot"], self.knights["mordred"])
        self._one_battle(self.knights["arthur"], self.knights["red_knight"])

        res = {}

        for knight in self.knights.values():
            res[knight["name"]] = knight["hp"]

        return res
