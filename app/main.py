from app.gentlemen import KNIGHTS
from app.chivalry import Chivalry


def battle(knightsconfig: dict) -> dict:
    lancelot = Chivalry(knightsconfig["lancelot"])
    arthur = Chivalry(knightsconfig["arthur"])
    mordred = Chivalry(knightsconfig["mordred"])
    red_knight = Chivalry(knightsconfig["red_knight"])
    lancelot.duel(mordred)
    arthur.duel(red_knight)
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
