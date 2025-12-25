from app.knight.knights import Knight


class Arthur(Knight):

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict = None) -> None:
        super().__init__(name=name, power=power, hp=hp, armour=armour,
                         weapon=weapon, potion=potion)
