from app.battle.knights_fight import round_n
from app.information_from import game
from app.information_from import user
from app.players.knights import Knights
from app.preparation.fight import prepare


knights = game.Game.KNIGHTS


def battle(knightsconfig: dict) -> dict:

    list_knights = [
        Knights(
            knight["name"],
            knight["hp"],
            knight["power"]
        )
        for knight in knightsconfig.values()
    ]
    prepare(list_knights, knightsconfig)

    return round_n(list_knights, user.UserInput.standard_order)


print(battle(knights))
