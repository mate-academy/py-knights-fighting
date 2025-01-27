from app.actions.sum_prot import sum_protection
from app.characteristics.potions import Potion
from app.characteristics.heros import Hero


def potion_preparation(potion: Potion) -> list:

    power = 0
    hp = 0
    protection = 0

    if "power" in potion.effect:
        power += potion.effect["power"]
    if "hp" in potion.effect:
        hp += potion.effect["hp"]
    if "protection" in potion.effect:
        protection += potion.effect["protection"]
    return [power, hp, protection]


def battle_preparations(knights: dict) -> list:

    heroes_list = []

    for key, knight_config in knights.items():

        protection = sum_protection(
            [armour for armour in knight_config["armour"]]
        )

        if knight_config["potion"] is not None:
            potion = Potion(
                knight_config["potion"]["name"],
                knight_config["potion"]["effect"]
            )
            potion_effects = potion_preparation(potion)
        else:
            potion_effects = [0, 0, 0]

        if "_" in key:
            name = key.replace("_", " ").title()
        else:
            name = key.capitalize()

        hero = Hero(
            name,
            knight_config["power"] + knight_config["weapon"]["power"]
            + potion_effects[0],
            knight_config["hp"] + potion_effects[1],
            protection + potion_effects[2]
        )

        heroes_list.append(hero)

    return heroes_list
