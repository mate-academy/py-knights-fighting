from app.Knights.knights import Knight


class Lancelot(Knight):
    def __init__(self, knights: dict) -> None:
        name = knights["lancelot"]["name"]
        hp = knights["lancelot"]["hp"]
        power = knights["lancelot"]["power"]
        armour = knights["lancelot"]["armour"]
        weapon = knights["lancelot"]["weapon"]
        potion = knights["lancelot"]["potion"]
        super().__init__(
            name=name,
            hp=hp,
            power=power,
            armour=armour,
            weapon=weapon,
            potion=potion
        )
