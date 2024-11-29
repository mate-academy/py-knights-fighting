from app.knight import Knight


def get_knight_from_database(knight: dict) -> Knight:
    knight_instance = Knight(
        name=knight.get("name"),
        power=knight.get("power"),
        hp=knight.get("hp"),
        armour=knight.get("armour"),
        weapon=knight.get("weapon"),
        potion=knight.get("potion")
    )
    return knight_instance


def knight_armoring_and_battle_preparation(knight: Knight) -> None:
    knight.set_knight_protection()
    knight.weapon_to_battle()
    knight.applying_potion()


def preparing_knight_to_battle(knight: dict) -> Knight:
    ready_knight = get_knight_from_database(knight)
    knight_armoring_and_battle_preparation(ready_knight)
    return ready_knight
