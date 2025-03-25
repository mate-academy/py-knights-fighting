from app.Knights.knights import Knight


class RedKnight(Knight):
    def __init__(self, knights: dict) -> None:
        name = knights["red_knight"]["name"]
        hp = knights["red_knight"]["hp"]
        power = knights["red_knight"]["power"]
        armour = knights["red_knight"]["armour"]
        weapon = knights["red_knight"]["weapon"]
        potion = knights["red_knight"]["potion"]
        super().__init__(
            name=name,
            hp=hp,
            power=power,
            armour=armour,
            weapon=weapon,
            potion=potion
        )
