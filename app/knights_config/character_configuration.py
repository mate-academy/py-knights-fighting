class Character:

    def __init__(self, name_knight: str, knight: dict) -> None:
        self.name = knight[name_knight]["name"]
        self.power = knight[name_knight]["power"]
        self.hp = knight[name_knight]["hp"]
        self.protection = 0
        for armour in knight[name_knight]["armour"]:
            self.protection += armour["protection"]
        self.power += knight[name_knight]["weapon"]["power"]

        if knight[name_knight]["potion"] is not None:
            if "power" in knight[name_knight]["potion"]["effect"]:
                self.power += knight[name_knight]["potion"]["effect"]["power"]
            if "protection" in knight[name_knight]["potion"]["effect"]:
                self.protection += \
                    knight[name_knight]["potion"]["effect"]["protection"]
            if "hp" in knight[name_knight]["potion"]["effect"]:
                self.hp += knight[name_knight]["potion"]["effect"]["hp"]
