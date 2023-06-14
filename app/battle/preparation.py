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
            for effect, value in self.knight["potion"]["effect"].items():
                self.knight[effect] += value
