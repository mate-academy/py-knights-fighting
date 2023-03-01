from app.battle.battle import Battle
from app.knights.knight import Knight
from app.knights.knights_parameters import KNIGHTS


def battle(knights):
    lancelot = Knight(
        name=knights.get("lancelot").get("name"),
        power=knights.get("lancelot").get("power"),
        hp=knights.get("lancelot").get("hp"),
        armour=knights.get("lancelot").get("armour"),
        weapon=knights.get("lancelot").get("weapon").get("power"),
        potion=knights.get("lancelot").get("potion")
    )
    arthur = Knight(
        name=knights.get("arthur").get("name"),
        power=knights.get("arthur").get("power"),
        hp=knights.get("arthur").get("hp"),
        armour=knights.get("arthur").get("armour"),
        weapon=knights.get("arthur").get("weapon").get("power"),
        potion=knights.get("arthur").get("potion")
    )
    mordred = Knight(
        name=knights.get("mordred").get("name"),
        power=knights.get("mordred").get("power"),
        hp=knights.get("mordred").get("hp"),
        armour=knights.get("mordred").get("armour"),
        weapon=knights.get("mordred").get("weapon").get("power"),
        potion=knights.get("mordred").get("potion")
    )
    red_knight = Knight(
        name=knights.get("red_knight").get("name"),
        power=knights.get("red_knight").get("power"),
        hp=knights.get("red_knight").get("hp"),
        armour=knights.get("red_knight").get("armour"),
        weapon=knights.get("red_knight").get("weapon").get("power"),
        potion=knights.get("red_knight").get("potion")
    )

    Battle.knight_equipped(lancelot)
    Battle.knight_equipped(arthur)
    Battle.knight_equipped(mordred)
    Battle.knight_equipped(red_knight)

    Battle.duel(lancelot, mordred)
    Battle.duel(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print({knight: hp for knight, hp in battle(KNIGHTS).items()})
