from app.knights.knights import Character


class UsePotion:
    def __init__(self, knight: Character):
        self.knight = knight

    def modify_power(self) -> None:
        if "power" in self.knight.potion["effect"]:
            self.knight.power += self.knight.potion["effect"]["power"]

    def modify_protection(self) -> None:
        if "protection" in self.knight.potion["effect"]:
            self.knight.protection += self.knight.potion["effect"]["protection"]

    def modify_hp(self) -> None:
        if "hp" in self.knight.potion["effect"]:
            self.knight.hp += self.knight.potion["effect"]["hp"]


    def use_all_potion(self):
        if self.knight.potion is not None:
            self.modify_power()
            self.modify_protection()
            self.modify_hp()