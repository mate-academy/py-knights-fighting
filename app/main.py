from app.players.knights import Knights
from app.preparation.fight import prepare
from app.battle.knights_fight import round_n
from app.information_from import user
from app.information_from import game


knights = game.Game.KNIGHTS


def battle(knightsconfig: dict) -> dict:

    # BATTLE PREPARATIONS:

    list_knights = [
        Knights(
            knight["name"],
            knight["hp"],
            knight["power"]
        )
        for knight in knightsconfig.values()
    ]
    prepare(list_knights, knightsconfig)

    # BATTLE:

    return round_n(list_knights, user.UserInput.standard_order)


print(battle(knights))
