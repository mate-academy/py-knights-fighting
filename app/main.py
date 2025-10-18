from app.fighter.fighters import Fighters
from app.fighter.fighter import Fighter


def check_fall(fighter: Fighter) -> None:
    if fighter.hp <= 0:
        fighter.hp = 0


def fight(fighter_one: Fighter, fighter_two: Fighter) -> None:
    fighter_one.hp -= fighter_two.power - fighter_one.protection
    fighter_two.hp -= fighter_one.power - fighter_two.protection
    check_fall(fighter_one)
    check_fall(fighter_two)


def battle(knights_config: dict) -> dict:
    fighters = Fighters(knights_config)
    fighters.create_fighters()
    fighters.initiate_fighters()

    lancelot, arthur, mordred, red_knight = fighters.get_fighters()

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
