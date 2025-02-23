class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight.get("name")
        self.hp = knight.get("hp")
        self.power = knight.get("power")
        self.armour_pieces = knight.get("armour")  # might have none
        self.weapon = knight.get("weapon")
        self.potion = knight.get("potion")  # might have none
        self.protection = 0

    def armour_up(self) -> None:
        for armor_piece in self.armour_pieces:
            self.protection += armor_piece.get("protection")

    def take_arms(self) -> None:
        self.power += self.weapon.get("power")

    def drink_potion(self) -> None:
        if self.potion is not None:
            if self.potion["effect"].get("power"):
                self.power += self.potion["effect"].get("power")

            if self.potion["effect"].get("protection"):
                self.protection += self.potion["effect"].get("protection")

            if self.potion["effect"].get("hp"):
                self.hp += self.potion["effect"].get("hp")


def prepare(contestants: dict) -> dict:
    lancelot = Knight(contestants.get("lancelot"))
    lancelot.armour_up()
    lancelot.take_arms()
    lancelot.drink_potion()

    arthur = Knight(contestants.get("arthur"))
    arthur.armour_up()
    arthur.take_arms()
    arthur.drink_potion()

    mordred = Knight(contestants.get("mordred"))
    mordred.armour_up()
    mordred.take_arms()
    mordred.drink_potion()

    red_knight = Knight(contestants.get("red_knight"))
    red_knight.armour_up()
    red_knight.take_arms()
    red_knight.drink_potion()

    return {
        "lancelot": lancelot,
        "arthur": arthur,
        "mordred": mordred,
        "red_knight": red_knight
    }
