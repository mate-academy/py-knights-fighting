class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

        # add "protection" stats from "armor" items
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

        # add "power" stats from "weapon" items
        self.power += self.weapon["power"]

        # add all stats from "potion" items
        if self.potion is not None:
            for key, value in self.potion["effect"].items():
                current_value = getattr(self, key)
                setattr(self, key, current_value + value)
