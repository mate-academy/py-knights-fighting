from app.battle.knights_prep import Knights


def knights_gear(knight: {dict}) -> dict:
    knights_list = {}
    for knight in knight.values():
        knight_model = Knights(
            name=knight["name"],
            hp=knight["hp"],
            power=knight["power"])

        knight_model.fight_prep(
            armours=knight["armour"],
            potion=knight["potion"],
            weapon=knight["weapon"])
        knights_list[knight_model.name] = knight_model
    return knights_list
