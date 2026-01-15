from app.characters.knights import Knight
from app.gears.armours import Armour
from app.gears.potions import Potion
from app.gears.weapons import Weapon


def prepare_characters(character_config: dict) -> dict[str: Knight]:
    characters = {}

    for description in character_config.values():
        name = description["name"]
        power = description["power"]
        hp = description["hp"]
        armours = Armour.create_armour_list(description["armour"])
        weapon = Weapon.create_weapon(description["weapon"])
        potion = Potion.create_potion(description["potion"])

        characters[name] = Knight(
            name=name,
            power=power,
            hp=hp,
            armour=armours,
            weapon=weapon,
            potion=potion
        )

    return characters


def fight(first_character: Knight, second_character: Knight) -> None:
    print(
        f"Let the fight between {first_character.name}"
        f"and {second_character.name} begin!"
    )
    first_character.fight_with(second_character)
    first_character.check_hp()
    second_character.check_hp()
    print("Fight is over!")


def show_battle_results(characters: dict) -> dict:
    return {
        character.name: character.hp
        for character in characters.values()
    }
