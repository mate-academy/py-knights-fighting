from app.Knights.knights import Knight


class Arthur(Knight):
    def __init__(self, knights: dict) -> None:
        name = knights["arthur"]["name"]
        hp = knights["arthur"]["hp"]
        power = knights["arthur"]["power"]
        armour = knights["arthur"]["armour"]
        weapon = knights["arthur"]["weapon"]
        potion = knights["arthur"]["potion"]
        super().__init__(
            name=name,
            hp=hp,
            power=power,
            armour=armour,
            weapon=weapon,
            potion=potion
        )
