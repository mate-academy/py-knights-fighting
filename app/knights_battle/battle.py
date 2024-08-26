from app.knights_battle.knight import Knight


def battle(knights_config: dict) -> dict:
    result = {}

    for element in knights_config:

        knight = Knight(
            name=knights_config[element]["name"],
            power=knights_config[element]["power"],
            hp=knights_config[element]["hp"],
            protection=0
        )

        knight.apply_armour(knights_config[element])
        knight.apply_weapon(knights_config[element])
        knight.apply_potion(knights_config[element])

        result[knight.name] = knight

    battle_list = ["Lancelot", "Mordred", "Arthur", "Red Knight"]

    for name in range(0, len(battle_list) // 2 + 1, 2):
        result[battle_list[name]].fight(result[battle_list[name + 1]])

    for name in range(len(battle_list)):
        result[battle_list[name]].check_if_someone_fell_in_battle()

    return {
        result["Lancelot"].name: result["Lancelot"].hp,
        result["Arthur"].name: result["Arthur"].hp,
        result["Mordred"].name: result["Mordred"].hp,
        result["Red Knight"].name: result["Red Knight"].hp,
    }
