class Knight:
    def __init__(self, alias: str) -> None:
        self.alias = alias
        self.protection = 0
        self.name = ""
        self.power = 0
        self.hp = 0


def set_knights(knights_data: dict) -> dict:
    knights = {}
    for fighter, preferences in knights_data.items():
        knight = Knight(fighter)
        knight.name = preferences["name"]
        knight.power = preferences["power"]
        knight.hp = preferences["hp"]

        for armour in preferences["armour"]:
            knight.protection += armour["protection"]

        knight.power += preferences["weapon"]["power"]

        if preferences["potion"] is not None:
            knight.power += preferences["potion"]["effect"].get("power", 0)
            knight.protection += (
                preferences["potion"]["effect"].get("protection", 0))
            knight.hp += preferences["potion"]["effect"].get("hp", 0)

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
