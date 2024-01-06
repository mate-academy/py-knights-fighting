class RedKnight:

    def __init__(self, pers_name: dict) -> None:
        self.pers_name = pers_name
        self.name = pers_name["name"]
        self.power = pers_name["power"]
        self.hp = pers_name["hp"]
        self.armour = pers_name["armour"]
        self.weapon = pers_name["weapon"]
        self.potion = pers_name["potion"]

    def red_knight_armour(self) -> list | None:
        if not self.armour:
            return None
        return self.armour

    def red_knight_weapon(self) -> dict:
        return self.weapon

    def red_knight_potion(self) -> dict | None:
        if self.potion is None:
            return None
        return self.potion["effect"]
