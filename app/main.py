from app.person.config import KNIGHTS
from app.person.knight import creator
from app.game.play import game


def battle(config: dict) -> dict:
    persons = creator(config)

    for name, person_obj in persons.items():
        person_obj.protection = 0
        for arm in person_obj.armour:
            person_obj.protection += arm["protection"]
        person_obj.power += person_obj.weapon["power"]
        if person_obj.potion is not None:
            if "power" in person_obj.potion["effect"]:
                person_obj.power += person_obj.potion["effect"]["power"]
            if "protection" in person_obj.potion["effect"]:
                person_obj.protection \
                    += person_obj.potion["effect"]["protection"]
            if "hp" in person_obj.potion["effect"]:
                person_obj.hp \
                    += person_obj.potion["effect"]["hp"]

    lancelot = persons["lancelot"]
    arthur = persons["arthur"]
    mordred = persons["mordred"]
    red_knight = persons["red_knight"]

    game(lancelot, mordred)
    game(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
