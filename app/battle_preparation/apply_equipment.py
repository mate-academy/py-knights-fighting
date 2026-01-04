class UpdateStats:
    def update_weapon(self) -> None:
        self.power += self.weapon["power"]

    def update_armour(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

    def apply_changes(self) -> None:
        self.update_weapon()
        self.update_armour()
        self.apply_potion()
