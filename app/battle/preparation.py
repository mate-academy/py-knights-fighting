from __future__ import annotations


class Preparation:
    def __init__(self, knight: dict) -> None:
        self.knight = knight
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion_if_exist()

    def apply_armour(self) -> None:
        self.knight["protection"] = 0
        for armour in self.knight["armour"]:
            self.knight["protection"] += armour["protection"]

    def apply_weapon(self) -> None:
        self.knight["power"] += self.knight["weapon"]["power"]

    def apply_potion_if_exist(self) -> None:
        if self.knight["potion"] is not None:
            if "power" in self.knight["potion"]["effect"]:
                self.knight["power"] +=\
                    self.knight["potion"]["effect"]["power"]

            if "protection" in self.knight["potion"]["effect"]:
                self.knight["protection"] +=\
                    self.knight["potion"]["effect"]["protection"]

            if "hp" in self.knight["potion"]["effect"]:
                self.knight["hp"] += self.knight["potion"]["effect"]["hp"]
