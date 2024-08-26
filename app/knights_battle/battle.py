from app.knights_battle.knight import Knight


def battle(knights_config: dict) -> dict:
    result = {}

    for element in knights_config:
        knight = Knight(name="", power=0, hp=0, protection=0)
        knight.adding_value_to_instance(knights_config[element])
        knight.adding_potion_to_instance(knights_config[element])
        result[knight.name] = knight

    battle_list = ["Lancelot", "Mordred", "Arthur", "Red Knight"]

    for kn_name in range(0, len(battle_list) // 2 + 1, 2):
        result[battle_list[kn_name]].fight(result[battle_list[kn_name + 1]])

    for kn_name in range(len(battle_list)):
        result[battle_list[kn_name]].check_if_someone_fell_in_battle()

    return {
        result["Lancelot"].name: result["Lancelot"].hp,
        result["Arthur"].name: result["Arthur"].hp,
        result["Mordred"].name: result["Mordred"].hp,
        result["Red Knight"].name: result["Red Knight"].hp,
    }
