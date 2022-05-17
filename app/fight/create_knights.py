from app.fight.knight import Knight


def create_knights(knight):
    knight = Knight(name=knight["name"],
                    power=knight["power"],
                    hp=knight["hp"],
                    armour=knight["armour"],
                    weapon=knight["weapon"],
                    potion=knight["potion"])
    return knight
