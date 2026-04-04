class Knight:
    def __init__(self, alias: str, preferences: dict) -> None:
        self.alias = alias
        self.protection = 0
        self.name = preferences["name"]
        self.power = preferences["power"]
        self.hp = preferences["hp"]

        for armour in preferences["armour"]:
            self.protection += armour["protection"]

        self.power += preferences["weapon"]["power"]

        if preferences["potion"] is not None:
            self.power += preferences["potion"]["effect"].get("power", 0)
            self.protection += (
                preferences["potion"]["effect"].get("protection", 0))
            self.hp += preferences["potion"]["effect"].get("hp", 0)


def set_knights(knights_data: dict) -> dict:
    knights = {}
    for fighter, preferences in knights_data.items():
        knight = Knight(fighter, preferences)

        knights[knight.alias] = knight

    return knights


def fighter_zero(fighter: Knight) -> None:
    if fighter.hp <= 0:
        fighter.hp = 0


def duel(fighter1: Knight, fighter2: Knight) -> None:
    fighter1.hp -= fighter2.power - fighter1.protection
    fighter2.hp -= fighter1.power - fighter2.protection

    # check if someone fell in battle
    fighter_zero(fighter1)
    fighter_zero(fighter2)
