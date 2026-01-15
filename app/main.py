from app.knights.knight_class import Knight, Weapon, Armour, Potion
from app.knights.knight_data import KNIGHTS
from app.battle import fight


def create_knight(knight_data: dict) -> Knight:
    weapon = Weapon(knight_data["weapon"]["name"],
                    knight_data["weapon"]["power"])

    armour = []
    for piece in knight_data["armour"]:
        armour.append(Armour(piece["part"], piece["protection"]))

    potion = None
    if knight_data["potion"] is not None:
        potion = Potion(knight_data["potion"]["name"],
                        knight_data["potion"]["effect"])

    knight = Knight(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"],
        armour=armour,
        weapon=weapon,
        potion=potion)

    return knight


def battle(knights_config: dict = KNIGHTS) -> dict:
    # Створи лицарів
    lancelot = create_knight(knights_config["lancelot"])
    arthur = create_knight(knights_config["arthur"])
    mordred = create_knight(knights_config["mordred"])
    red_knight = create_knight(knights_config["red_knight"])

    # Запусти бої
    result_1 = fight(lancelot, mordred)
    result_2 = fight(arthur, red_knight)

    # Об’єднай результати в один словник
    return {**result_1, **result_2}


if __name__ == "__main__":
    results = battle()
