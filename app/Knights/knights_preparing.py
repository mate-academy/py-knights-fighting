from app.Knights.constructor import KnightConstructor


class KnightPreparing(KnightConstructor):
    def prepare_for_fight(self) -> None:
        self.apply_armor()
        self.apply_weapon()
        self.apply_potion_if_exist()

    def apply_armor(self) -> list:
        for armour in self.armour:
            self.protection += armour["protection"]
        return self.armour

    def apply_weapon(self) -> int:
        self.power = self.power + self.weapon["power"]
        return self.power

    def apply_potion_if_exist(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
