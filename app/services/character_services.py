from app.character.armour import Armour
from app.character.dto import PotionDto, CharacterDto, ArmourDto
from app.character.effect import Effect
from app.character.knight import Knight
from app.character.potion import Potion
from app.character.weapon import Weapon


def get_armour_list(armours: list[ArmourDto]) -> list[Armour]:
    return [
        Armour(part=armour["part"], protection=armour["protection"])
        for armour in armours
    ]


def create_potion(potion: PotionDto | None) -> Potion | None:
    if potion is None:
        return None

    effect = potion["effect"]

    return Potion(
        name=potion.get("name"),
        effect=Effect(
            power=effect.get("power"),
            hp=effect.get("hp"),
            protection=effect.get("protection")
        ),
    )


def create_character(data: CharacterDto) -> Knight:
    return Knight(
        name=data["name"],
        power=data["power"],
        hp=data["hp"],
        armour=get_armour_list(data["armour"]),
        weapon=Weapon(
            power=data["weapon"]["power"],
            name=data["weapon"]["name"],
        ),
        potion=create_potion(data["potion"])
    )


def get_characters_as_class(knights: dict) -> list[Knight]:
    return [create_character(knights[knight]) for knight in knights]
