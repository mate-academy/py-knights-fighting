from app.preparation.knight import Knight
from app.preparation.equipment import Armour, Weapon, Potion
from app.battle.battle import Battle


def battle(stats: dict) -> dict:
    knights = {}

    for stat in stats.values():
        # Create Knights
        knights[stat["name"]] = (
            Knight(stat["name"], stat["power"], stat["hp"])
        )

        # Add Equipment
        for knight in knights.values():
            if knight.name == stat["name"]:
                # Weapon
                knight.weapon = (
                    Weapon(stat["weapon"]["name"], stat["weapon"]["power"])
                )

                # Armour
                if stat["armour"] is not None:
                    knight.armour = [
                        Armour(part["part"], part["protection"])
                        for part in stat["armour"]
                    ]

                # Potion
                if stat["potion"] is not None:
                    knight.potion = Potion(
                        stat["potion"]["name"], **stat["potion"]["effect"]
                    )

    for knight in knights.values():
        # Apply armour
        for part in knight.armour:
            knight.apply_armour(part.protection)

        # Apply weapon
        knight.apply_weapon(knight.weapon)

        # Apply potion
        if hasattr(knight, "potion"):
            knight.apply_potion(knight.potion)

    # Battles begin
    lancelot = knights["Lancelot"]
    mordred = knights["Mordred"]
    arthur = knights["Arthur"]
    red_knight = knights["Red Knight"]

    # Battle 1
    Battle.fight(lancelot, mordred)
    # Battle 2
    Battle.fight(arthur, red_knight)

    # Check if knights have fallen
    for knight in knights.values():
        Battle.was_slain(knight)

    # Return results of battles
    return {
        knight.name: knight.hp for knight in knights.values()
    }
