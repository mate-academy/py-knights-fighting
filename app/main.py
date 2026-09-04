from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:

    knights_list = {
        knight["name"]: Knight(
            knight["name"],
            knight["hp"],
            knight["power"],
            knight["armour"],
            knight["weapon"],
            knight["potion"]
        ) for knight in knights_config.values()
    }

    for knight in knights_list.values():
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    knights_list["Lancelot"].battle_with(knights_list["Mordred"])
    knights_list["Arthur"].battle_with(knights_list["Red Knight"])

    return {
        knights_list["Lancelot"].name: knights_list["Lancelot"].hp,
        knights_list["Arthur"].name: knights_list["Arthur"].hp,
        knights_list["Mordred"].name: knights_list["Mordred"].hp,
        knights_list["Red Knight"].name: knights_list["Red Knight"].hp,
    }
