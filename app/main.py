from app.people.KNIGHTS import KNIGHTS
from app.transform import transform_knights


def battle(knights: dict) -> dict:
    knights_battle = transform_knights(knights)
    for knight in knights_battle.values():
        knight.equip()
    knights_battle["lancelot"].fight(knights_battle["mordred"])
    knights_battle["arthur"].fight(knights_battle["red_knight"])
    return {
        knights_battle["lancelot"].name: knights_battle["lancelot"].hp,
        knights_battle["arthur"].name: knights_battle["arthur"].hp,
        knights_battle["mordred"].name: knights_battle["mordred"].hp,
        knights_battle["red_knight"].name: knights_battle["red_knight"].hp,
    }


print(battle(KNIGHTS))
