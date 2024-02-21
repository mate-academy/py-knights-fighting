class Player:

    def __init__(self, pers_name: dict) -> None:
        self.name = pers_name["name"]
        self.power = pers_name["power"]
        self.hp = pers_name["hp"]
        self.armour = pers_name["armour"]
        self.weapon = pers_name["weapon"]
        self.potion = pers_name["potion"]

        setattr(Player, "protection", 0)
