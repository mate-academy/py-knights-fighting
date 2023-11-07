from app.input import KNIGHTS
from app.knights import Knights


def battle(knights_config: dict) -> dict:
    knight_instances = []
    for player, info in knights_config.items():
        name, power, hp, armours, weapons, potion = info.values()

        knight_instance = Knights(
            name=name,
            power=power,
            hp=hp
        )
        if armours:
            protection = []
            for armour in armours:
                protection.append(armour["protection"])
            knight_instance.get_protection(protection)

        knight_instance.get_power(weapons["power"])

        if potion:
            if "power" in potion["effect"]:
                knight_instance.get_power(potion["effect"]["power"])
            if "hp" in potion["effect"]:
                knight_instance.get_hp(potion["effect"]["hp"])
            if "protection" in potion["effect"]:
                knight_instance.get_protection(potion["effect"]["protection"])
        knight_instances.append(knight_instance)

    lancelot = knight_instances[0]
    mordred = knight_instances[2]
    lancelot - mordred
    mordred - lancelot

    arthur = knight_instances[1]
    red_knight = knight_instances[3]
    arthur - red_knight
    red_knight - arthur

    return {
        lancelot.name: max(lancelot.hp, 0),
        arthur.name: max(arthur.hp, 0),
        mordred.name: max(mordred.hp, 0),
        red_knight.name: max(red_knight.hp, 0),
    }


print(battle(KNIGHTS))
