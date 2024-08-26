from app.knights_battle.knight import Knight


def battle(knights_config: dict) -> dict:
    result = {}

    for knight in knights_config:

        instance = Knight(
            name=knights_config[knight]["name"],
            power=knights_config[knight]["power"],
            hp=knights_config[knight]["hp"],
            protection=0,
            knight=knights_config[knight],
        )
        result[instance.name] = instance

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
