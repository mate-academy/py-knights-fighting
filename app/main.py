from app.players.knight import Knight
from app.battles.duel import duel


def battle(knights_config: dict) -> dict:
    knights = list()

    lancelot = Knight.create_from_dict(knights_config["lancelot"])
    lancelot.equip_armour_all()
    lancelot.equip_weapon()
    lancelot.drink_potion()
    knights.append(lancelot)

    arthur = Knight.create_from_dict(knights_config["arthur"])
    arthur.prepare_for_battle()
    knights.append(arthur)

    mordred = Knight.create_from_dict(knights_config["mordred"])
    mordred.prepare_for_battle()
    knights.append(mordred)

    red_knight = Knight.create_from_dict(knights_config["red_knight"])
    red_knight.prepare_for_battle()
    knights.append(red_knight)

    duel(lancelot, mordred)
    duel(arthur, red_knight)

    return {knight.name: knight.hp for knight in knights}
