from app.knights.knight import Knight


def battle(knightsConfig):
    knights = []

    for knight_config in knightsConfig.values():
        name = knight_config["name"]
        power = knight_config["power"]
        hp = knight_config["hp"]
        armour = knight_config["armour"]
        weapon = knight_config["weapon"]
        potion = knight_config["potion"]

        knight = Knight(name, power, hp, armour, weapon, potion)
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

        knights.append(knight)

    results = {}

    for knight in knights:
        remaining_knights = knights.copy()
        remaining_knights.remove(knight)

        for opponent in remaining_knights:
            knight_hp = knight.hp - opponent.power + knight.protection
            opponent_hp = opponent.hp - knight.power + opponent.protection

            knight_hp = max(knight_hp, 0)
            opponent_hp = max(opponent_hp, 0)

            results[knight.name] = knight_hp
            results[opponent.name] = opponent_hp

    return results