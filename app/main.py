from app.gentlemen import KNIGHTS
from app.knight import Knight


def battle(knightsconfig: dict) -> dict:
    lancelot = Knight(knightsconfig["lancelot"])
    arthur = Knight(knightsconfig["arthur"])
    mordred = Knight(knightsconfig["mordred"])
    red_knight = Knight(knightsconfig["red_knight"])
    return lancelot.duel(mordred) | arthur.duel(red_knight)


print(battle(KNIGHTS))
