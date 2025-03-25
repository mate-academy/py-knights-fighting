from app.Knights.knights import Knight


class Mordred(Knight):
    def __init__(self, knights: dict) -> None:
        name = knights["mordred"]["name"]
        hp = knights["mordred"]["hp"]
        power = knights["mordred"]["power"]
        armour = knights["mordred"]["armour"]
        weapon = knights["mordred"]["weapon"]
        potion = knights["mordred"]["potion"]
        super().__init__(
            name=name,
            hp=hp,
            power=power,
            armour=armour,
            weapon=weapon,
            potion=potion
        )
