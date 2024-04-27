from app.armour import Armour
from app.knight import Knight
from app.potion import Potion
from app.weapon import Weapon


def battle(knights_config: dict) -> dict:
    knights = []

    for knight_data in knights_config.values():
        knight = Knight(knight_data["name"], knight_data["power"], knight_data["hp"])

        # Equip armour
        for armour_data in knight_data["armour"]:
            armour = Armour(armour_data["part"], armour_data["protection"])
            knight.get_armour(armour)

        # Equip weapon using dictionary unpacking
        weapon = Weapon(**knight_data["weapon"])
        knight.get_weapon(weapon)

        # Equip potion (if available) using dictionary unpacking
        if knight_data["potion"] is not None:
            potion = Potion(**knight_data["potion"])
            knight.get_potion(potion)

        knights.append(knight)

    # Identify specific knights for battle
    lancelot, arthur, mordred, red_knight = None, None, None, None
    for knight in knights:
        if knight.name == "Lancelot":
            lancelot = knight
        elif knight.name == "Arthur":
            arthur = knight
        elif knight.name == "Mordred":
            mordred = knight
        elif knight.name == "Red Knight":
            red_knight = knight

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.battle(mordred)
    mordred.battle(lancelot)

    # 2 Arthur vs Red Knight:
    arthur.battle(red_knight)
    red_knight.battle(arthur)

    # Return battle results
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
