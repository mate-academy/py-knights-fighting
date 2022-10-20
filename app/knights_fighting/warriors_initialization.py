from app.knights_fighting.class_of_warrior import Warrior


def heroes_initialization(knights_config: dict) -> list:
    """
    Character initialization function

    In this function, we create instances of the warrior class
    and apply the methods of this class to them.
    :param knights_config: dict
    :return: list
    """

    # Declare 4 variables - the names of the heroes
    lancelot, arthur, mordred, red_knight = None, None, None, None
    # Create instances of the class for each hero, apply methods to them
    for stat in knights_config.values():
        if stat["name"] == "Lancelot":
            lancelot = Warrior(stat["name"], stat["power"], stat["hp"])
            lancelot.apply_armour(stat["armour"])
            lancelot.apply_weapon(stat["weapon"])
            lancelot.apply_potion(stat["potion"])

        if stat["name"] == "Artur":
            arthur = Warrior(stat["name"], stat["power"], stat["hp"])
            arthur.apply_armour(stat["armour"])
            arthur.apply_weapon(stat["weapon"])
            arthur.apply_potion(stat["potion"])

        if stat["name"] == "Mordred":
            mordred = Warrior(stat["name"], stat["power"], stat["hp"])
            mordred.apply_armour(stat["armour"])
            mordred.apply_weapon(stat["weapon"])
            mordred.apply_potion(stat["potion"])

        if stat["name"] == "Red Knight":
            red_knight = Warrior(stat["name"], stat["power"], stat["hp"])
            red_knight.apply_armour(stat["armour"])
            red_knight.apply_weapon(stat["weapon"])
            red_knight.apply_potion(stat["potion"])

    return [lancelot, arthur, mordred, red_knight]
