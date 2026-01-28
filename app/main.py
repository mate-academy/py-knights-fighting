from app.character.CharacterParser import CharacterParser
from app.territory.Arena import Arena
from app.variables import KNIGHTS


def battle(knights_config: dict) -> dict:

    list_of_characters = CharacterParser.parse(knights_config)

    for character in list_of_characters:
        character.prepare_for_battle()

    arena1 = Arena()
    arena2 = Arena()

    for character in list_of_characters:
        if character.name == "Lancelot":
            arena1.add_participant(character)
        if character.name == "Mordred":
            arena1.add_participant(character)
        if character.name == "Arthur":
            arena2.add_participant(character)
        if character.name == "Red Knight":
            arena2.add_participant(character)

    arena1.start_battle()
    arena2.start_battle()

    return {character.name : character.hp for character in list_of_characters}


if __name__ == "__main__":
    print(battle(KNIGHTS))
