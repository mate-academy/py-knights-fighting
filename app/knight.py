class Knight:

    def __init__(self, knight_info: dict) -> None:
        self.name = knight_info["name"]
        self.power = knight_info["power"]
        self.hp = knight_info["hp"]
        self.armour = knight_info["armour"]
        self.weapon = knight_info["weapon"]
        self.potion = knight_info["potion"]
        self.protection = 0

    def apply_armour(self) -> None:
        if self.armour:
            for armour in self.armour:
                self.protection += armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            for key, value in self.potion["effect"].items():
                if key == "hp":
                    self.hp += value
                if key == "power":
                    self.power += value
                if key == "protection":
                    self.protection += value

    def get_prepared(self) -> None:
        self.apply_weapon()
        self.apply_armour()
        self.apply_potion()


def create_knights(knights: dict) -> dict:
    knights_dict = {}
    for knight, knight_info in knights.items():
        knights_dict[knight_info["name"]] = Knight(knight_info)
    return knights_dict
